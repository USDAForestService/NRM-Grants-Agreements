import datetime
import uuid

from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Grant


class GrantForm(forms.ModelForm):
    # We're using modelChoiceField here, but as the DB is currently configured passing choices to a ChoiceField
    # would work just as well (maybe better)
    # TO-DO: Ideally we would migrate to Categories being just a list of cats,
    # with Grant having an FK to that table, so we could avoid these sorts of shenanigans.
    project_category = forms.ModelChoiceField(
        queryset=Category.objects.order_by("category_desc").distinct("category_desc"),
    )

    class Meta:
        model = Grant
        exclude = [
            "application_id",
        ]
        widgets = {
            "areas_effected": forms.Textarea(attrs={"cols": 80, "rows": 10}),
        }

    def __init__(self, *args, **kwargs):
        """
        A quick init to add some classes on some fields, since we don't need to override the widget,
        and add a custom field or two.
        """
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields["proj_title"].widget.attrs["class"] += " text-wide"

        # If we're modifying an existing instance in a changeform we'll need to set the initial value
        # for project_category, because we don't have a proper FK from Grant
        if self.instance:
            cat_init_cn = Category.objects.get(grant=self.instance).cn
            self.fields["project_category"].initial = cat_init_cn

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
        return instance
