import datetime
import uuid

from django import forms
from django.core.exceptions import ValidationError

from .models import Grant
from contacts.models import AccomplishmentInstrument, Contact


class GrantForm(forms.ModelForm):
    class Meta:
        model = Grant
        exclude = [
            "application_id",
        ]
        widgets = {
            "areas_effected": forms.Textarea(attrs={"cols": 80, "rows": 10}),
        }

    org_select = forms.ModelChoiceField(
        label="Organization",
        queryset=Contact.objects.filter(
            cn__in=AccomplishmentInstrument.objects.values("managing_contact")
        ).distinct(),
    )

    def __init__(self, *args, **kwargs):
        """A quick init to add some classes on some fields, since we don't need to override the widget."""
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields["proj_title"].widget.attrs["class"] += " text-wide"

        # If we're modifying an existing instance in a changeform we'll need
        # to set the initial value for org, because we don't have an FK
        # directly on Grant
        if self.instance:
            self.fields["org_select"].initial = self.instance.org

    def clean_state_eo_date(self):
        """
        Ensures that if State EO Code is Yes, then a date must be entered.
        """
        cleaned_data = super().clean()
        eo_code = cleaned_data.get("state_eo_code")
        eo_date = cleaned_data.get("state_eo_date")

        if eo_code == "Y" and not eo_date:
            raise ValidationError(
                "If this agreement is subject to state EO, you must enter an EO date."
            )

    def save(self, commit=True):
        """
        Ensures on save we generate and save several values:
        * A new CN/PK
        * Updated `status_date` if new or status has chanaged.
        * `created_in_instance` and `modified_in_instance`

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
        # TO-DO: figure out a better way to know the correct region. Maybe from contacts table?
        year_char = datetime.date.today().strftime("%y")[1:]
        short_uuid = str(uuid.uuid4())[:8]
        # Assuming we end up keeping instance_ids as a useful thing we'll have to learn how to
        # capture them correctly rather than just using a hard-coded value as we are here.
        instance_id = "10602"
        instance.cn = "%s%s%s0%s" % (year_char, "6", short_uuid, instance_id)

        # if some undetermined sequence of events happens, we will need to update `status`
        # if that happens, we would need to update status_date, too.
        # but we only need to do this check on existing record saves, when we need to update the defaults
        if instance.cn and "status" in self.changed_data:
            instance.status_date = datetime.datetime.now()

        if instance.cn and "wppp_status" in self.changed_data:
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
            # print("initial value: ", self.initial["org_select"])
            if instance.cn and "org_select" in self.changed_data:
                # first, is there an existing ai? Note that the 1:1 relationship is untrustworthy.
                # Because we don't trust it and we're using first(), we won't use get_or_create() either.
                ai = AccomplishmentInstrument.objects.filter(grant=instance).first()
                if not ai:
                    ai = AccomplishmentInstrument(grant_id=instance.cn)
                ai.managing_contact = Contact.objects.get(
                    cn=self.data.get("org_select")
                )
                ai.save()

        return instance
