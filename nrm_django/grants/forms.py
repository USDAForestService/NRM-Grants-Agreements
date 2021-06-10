import datetime
import uuid

from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Grant
from contacts.models import AccomplishmentInstrument, Contact

instance_id = "10602"


class MinGrantForm(forms.ModelForm):
    """
    Defines the minimum viable Grant/proposal creation form.
    """

    class Meta:
        model = Grant
        fields = [
            "proj_title",
            "proj_desc",
            "app_submit_date",
            "app_received_date",
            "proposed_start_date",
            "proposed_end_date",
            "progrm_responsibility_type",
            "advance_allowed_ind",
            "master_fed_id",
            "state_eo_date",
            "state_eo_code",
            "application_type",
            "app_submission_type",
            "proj_rwu",
            "journal_ind",
            "proj_science_cd",
            "research_type",
        ]

    def save(self, commit=True):
        """
        On initial save we generate several values:
        * A new CN/PK
        * `created_in_instance`
        * `modified_in_instance`

        Note that the instance ID is currently hard-coded.
        It may have no value beyond mimicking the legacy system,
        but if it is needed we will still need to learn how to capture it.
        """
        instance = super().save(commit=False)
        # first, we're gonna have to create our cn/pk
        # * First character: Year
        # * Second character: Region
        # * Trailing characters: The instance created in
        # * Middle characters: some unique ID
        # TO-DO: figure out a better way to know the correct region.
        # Maybe from contacts table?
        # Assuming we end up keeping instance_ids as a useful thing we'll have to learn how to
        # capture them correctly rather than just using a hard-coded value as we are here.
        year_char = datetime.date.today().strftime("%y")[1:]
        short_uuid = str(uuid.uuid4())[:8]
        instance.cn = "%s%s%s0%s" % (year_char, "6", short_uuid, instance_id)

        # stubbing out foo_in_instance rather than making defaults
        # since we don't know yet how to populate them correctly or what the values mean.
        # eventually we'll have some sort of check or logic here.
        instance.created_in_instance = instance.modified_in_instance = instance_id

        if commit:
            instance.save()
        return instance

    def clean_state_eo_code(self):
        """
        Ensures that if State EO Code is Yes, then a date must be entered.
        """
        eo_code = self.cleaned_data["state_eo_code"]

        if eo_code and eo_code.lower() == "y":
            if not self.cleaned_data["state_eo_date"]:
                raise ValidationError(
                    "If this agreement is subject to state EO, you must enter an EO date."
                )
        return eo_code


class GrantUpdateForm(forms.ModelForm):
    """
    On update, we'll make all fields editable.
    """

    # First we need to sort out project category.
    # We're using modelChoiceField, but it may make more sense to use a ChoiceField.
    # The actual queryset gets set down below in `init`
    # TO-DO: Ideally we would migrate to Categories being just a list of cats,
    # with Grant having an FK to that table, so we could avoid these sorts of shenanigans.
    cat_set = Category.objects.order_by("category_desc").distinct("category_desc")

    project_category = forms.ModelChoiceField(
        label="Project category",
        queryset=cat_set,
        required=False,
        help_text="If 'International Activities' is 'Yes', you must choose a category.",
    )
    org_select = forms.ModelChoiceField(
        label="Organization",
        queryset=Contact.objects.filter(
            cn__in=AccomplishmentInstrument.objects.values("managing_contact")
        ).distinct(),
    )

    class Meta:
        model = Grant
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GrantUpdateForm, self).__init__(*args, **kwargs)

        # If we're modifying an existing instance we'll need to manually
        # set the initial value for org, because we don't have an FK on Grant
        if self.instance:
            print("self instance org is", self.instance.org)
            self.fields["org_select"].initial = self.instance.org

        # We'll also need to set the initial project_category.
        # Because we used distinct() to toss out duplicate Cats, we have to find one
        # that matches whatever one was set on the current Grant so it looks right.
        if self.instance.cn:
            try:
                this_cat = Category.objects.get(grant=self.instance)
                # if we dropped this cat becuase of the distinct() on cat_set, we need to add it back in:
                if this_cat not in self.cat_set:
                    # there is a category in cat_set with this_cat's same
                    # category_desc. Swap that one out for this one.
                    cat_ids = [cat.cn for cat in self.cat_set]
                    replace_me = (
                        Category.objects.filter(
                            cn__in=cat_ids, category_desc=this_cat.category_desc
                        )
                        .first()
                        .cn
                    )
                    cat_ids[cat_ids.index(replace_me)] = this_cat.cn
                    # reconstruct the queryset
                    self.cat_set = Category.objects.filter(cn__in=cat_ids)
                self.fields["project_category"].initial = this_cat.cn
            except Category.DoesNotExist:
                pass

    def clean_project_category(self):
        """
        Ensures at least one category is set if international_agreement_ind is true
        """
        cleaned_data = super().clean()
        intl_act = cleaned_data.get("international_act_ind")
        if intl_act and intl_act.lower().startswith("y"):
            if not cleaned_data.get("project_category"):
                raise ValidationError(
                    "International agreements must have a program category."
                )
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # if some undetermined sequence of events happens, we will need to update `status`
        # if that happens, we would need to update status_date, too.

        if "wppp_status" in self.changed_data:
            instance.wppp_status_date = datetime.datetime.now()

        # stubbing out foo_in_instance rather than making defaults
        # since we don't know yet how to populate them correctly or what the values mean.
        # eventually we'll have some sort of check or logic here.
        instance.created_in_instance = instance.modified_in_instance = instance_id

        if commit:
            instance.save()

            # org is actually a property of the accomplishment instrument.
            # When it changes, we need to change the change the value over there.
            # To-Do: in the future, this should probably be migrated into grant itself
            # since it's a 1:1 anyway.
            if instance.cn and "org_select" in self.changed_data:
                # first, is there an existing ai? Note that the 1:1 relationship is untrustworthy.
                # Because we don't trust it and we're using first(), we won't use get_or_create() either.
                ai = AccomplishmentInstrument.objects.filter(grant=instance).first()
                if not ai:
                    ai = AccomplishmentInstrument(grant_id=instance.cn)
                ai.managing_contact = Contact.objects.get(
                    cn=self.data.get("org_select")
                )
                # ai.save() TO-DO: Uncomment this when we've fixed AIs in #222

        # We need to create a new category if one does not already exist for this grant.
        # It might make sense do make this a signal or some other post_save() mechanism,
        # since it's dependent on the grant being in the DB.
        # TO-DO: when we migrate to a proper FK, remove all of this
        if "project_category" in self.changed_data:
            # temp_cat is the category the user selected from the
            # limited set of cats defined in cat_set above.
            # We want the raw value, so we're not using cleaned_data
            temp_cat = Category.objects.get(cn=self.data.get("project_category"))
            Category.objects.get_or_create(
                cn=str(uuid.uuid4().hex),
                grant=instance,
                category_cd=temp_cat.category_cd,
                category_desc=temp_cat.category_desc,
            )

        return instance
