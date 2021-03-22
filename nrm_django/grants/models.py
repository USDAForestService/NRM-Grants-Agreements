from django.db import models
from django.utils.safestring import mark_safe

from .choices import (
    AB_CHOICES,
    BOOL_CHOICES,
    FED_ID_REGION_CHOICES,
    FED_ID_TYPE_CHOICES,
    STATUS_CHOICES,
    APPLICATION_TYPE_CHOICES,
    APP_SUBMISSION_TYPE_CHOICES,
    YEAR_CHOICES,
)


class Grant(models.Model):
    """
    Defines a grant and it's status through the full workflow.

    Has a lot of related info in here, too.
    """

    cn = models.CharField(max_length=34, primary_key=True, editable=False)
    proj_title = models.CharField("Project title", max_length=200)
    proj_status = models.CharField(
        "Project status", max_length=15, blank=True, null=True, choices=AB_CHOICES
    )
    # Sys-generated, once initial proposal saved. Control number.
    # Older field, not user viewable. Only used for historical records.
    application_id = models.CharField(max_length=34, editable=False)
    application_type = models.CharField(max_length=30, choices=APPLICATION_TYPE_CHOICES)
    app_submission_type = models.CharField(
        "Application submission type",
        max_length=100,
        choices=APP_SUBMISSION_TYPE_CHOICES,
    )
    app_submit_date = models.DateField("Application submitted")
    app_received_date = models.DateField("Application received")
    # No longer utilized, not in the application.
    hhs_payment_ind = models.CharField(max_length=1, default="N", editable=False)

    proposed_start_date = models.DateField()
    proposed_end_date = models.DateField()
    # this was never implemented in the front end but the desire is that sys admins
    # and help desk should be able to lock a record so it cannot be edited
    # (unless they unlock it). For now, marking it as not-editable.
    locked_ind = models.CharField(
        choices=BOOL_CHOICES, max_length=1, default="N", editable=False
    )
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    status_date = models.DateField()
    # Should record current user on save()
    created_by = models.CharField(max_length=30, editable=False)  # FK?
    created_date = models.DateField(auto_now_add=True)
    # Sys generated field. Comes from RACA, says what instance of the application it is.
    # We need to determine how to generate it.
    created_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, editable=False
    )
    # There may be a subset of fields that should trigger this but it will be the current
    # user that did the modification
    modified_by = models.CharField(max_length=30, blank=True, null=True)  # FK?
    modified_date = models.DateField(blank=True, null=True, auto_now=True)
    # Same as created_in_instance, we need to determine how to generate this.
    modified_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True, editable=False
    )
    # These are the fields agreement numbers are derived from.
    # Few people interact with them directly though.
    fed_id_fy = models.CharField(
        max_length=4, blank=True, null=True, choices=YEAR_CHOICES
    )
    fed_id_type = models.CharField(
        max_length=2, blank=True, null=True, choices=FED_ID_TYPE_CHOICES
    )
    fed_id_agency = models.CharField(max_length=2, blank=True, null=True)
    fed_id_region = models.CharField(
        max_length=2, blank=True, null=True, choices=FED_ID_REGION_CHOICES
    )
    fed_id_unit = models.CharField(max_length=2, blank=True, null=True)
    fed_id_subunit = models.CharField(max_length=2, blank=True, null=True)
    fed_id_seq = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )

    # Fields describing project(s) and significant dates.
    proj_type = models.CharField(
        "Project Type", max_length=3, blank=True, null=True, choices=AB_CHOICES
    )
    proj_desc = models.TextField(
        "Project description", max_length=2000, blank=True, null=True
    )
    proj_received_dt = models.DateField("Project received date", blank=True, null=True)
    proj_execution_dt = models.DateField(
        "Project execution date", blank=True, null=True
    )
    proj_start_dt = models.DateField("Start date", blank=True, null=True)
    proj_obligation_dt = models.DateField(
        "Project obligation date", blank=True, null=True
    )
    proj_expiration_dt = models.DateField("Expires", blank=True, null=True)
    proj_close_dt = models.DateField("Project close date", blank=True, null=True)
    proj_cancellation_dt = models.DateField(
        "Project cancellation date", blank=True, null=True
    )
    proj_rwu = models.CharField(max_length=10, blank=True, null=True)  # What's RWU
    proj_cfda_no = models.CharField(
        "Project CFDA", max_length=40, blank=True, null=True
    )
    proj_science_cd = models.CharField(
        "Project Science CD", max_length=3, blank=True, null=True
    )  # What's science CD?
    project_congressional_district = models.CharField(
        max_length=40, blank=True, null=True
    )

    date_mailed = models.DateField(blank=True, null=True)
    date_signed = models.DateField(blank=True, null=True)
    comments = models.TextField(max_length=2000, blank=True, null=True)

    extramural_ind = models.CharField(
        "Extramural", choices=BOOL_CHOICES, max_length=1, null=True
    )  # should be a boolean, but appears to be null in some DB instances
    research_type = models.CharField(max_length=1, blank=True, null=True)
    journal_ind = models.CharField("Journal", max_length=1, blank=True, null=True)
    mod_number = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )
    orig_fed_id = models.CharField(
        "Original Fed ID", max_length=120, blank=True, null=True
    )
    master_fed_id = models.CharField(
        "Master Fed ID", max_length=120, blank=True, null=True
    )
    aop_ind = models.CharField(
        "AOP", choices=BOOL_CHOICES, max_length=1, null=True
    )  # should be a boolean, but appears to be null in some DB instances
    geo_type = models.CharField(max_length=2, blank=True, null=True)
    managing_state_county = models.CharField(max_length=240, blank=True, null=True)
    areas_effected = models.CharField(max_length=200, blank=True, null=True)
    ffin = models.CharField(max_length=40, blank=True, null=True)

    # State fields
    state_identifier = models.CharField(
        max_length=40, blank=True, null=True
    )  # choices? FK?
    state_eo_code = models.CharField(max_length=1, blank=True, null=True)
    state_eo_date = models.DateField(blank=True, null=True)

    # EST Fund fields
    fed_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    applicant_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    state_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    local_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    pi_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    oth_est_fund = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    reroute_from = models.CharField(max_length=10, blank=True, null=True)
    reroute_date = models.DateField(blank=True, null=True)
    certificaion_date = models.DateField("Certification date", blank=True, null=True)
    ffis_doc_id = models.CharField("FFIS Doc", max_length=11, blank=True, null=True)
    applicant_name = models.CharField(
        "Applicant/Cooperator Name", max_length=200, blank=True, null=True
    )
    international_act_ind = models.CharField(
        "International Act", choices=BOOL_CHOICES, max_length=1, null=True, default="N"
    )
    advance_allowed_ind = models.CharField(
        "Advance Allowed", choices=BOOL_CHOICES, max_length=1, null=True, default="N"
    )
    authority_approval = models.CharField(
        max_length=1, blank=True, null=True, choices=BOOL_CHOICES, default="N"
    )
    authority = models.CharField(
        max_length=1, blank=True, null=True, choices=BOOL_CHOICES, default="N"
    )
    format = models.CharField(
        max_length=1, blank=True, null=True, choices=BOOL_CHOICES, default="N"
    )  # we may need to safely rename this column
    other_approval = models.CharField(
        max_length=1, blank=True, null=True, choices=BOOL_CHOICES, default="N"
    )
    master_agreement_ind = models.CharField(
        max_length=1, blank=True, null=True
    )  # boolean indicator
    progrm_responsibility_type = models.CharField(
        "Program Responsibility Type", max_length=30, blank=True, null=True
    )  # choices?
    # What is wppp?
    wppp_status = models.CharField(max_length=40, blank=True, null=True)
    wppp_status_date = models.DateField(blank=True, null=True)
    cooperator_agreement_number = models.CharField(
        max_length=34, blank=True, null=True
    )  # Is this used to key to a cooperator agreement?
    gid = models.CharField("Agreement Number", max_length=16, blank=True, null=True)
    admin_open = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        db_table = "ii_grants"
        verbose_name = "Grant/Agreement"
        verbose_name_plural = "Grants and Agreements"

    def __str__(self):
        return self.proj_title

    def pretty_name(self):
        return "%s" % self.proj_title.title()

    pretty_name.short_description = "Project Title"

    def pretty_cooperator_name(self):
        """
        Prettifies the applicant/cooperator name.
        If the name is all uppercase, it transforms it to title case.
        If the name is not uppercase, it assumes the name was input as intended and does nothing.
        If the name does not exist, it returns an empty string (no change).
        """
        if self.applicant_name:
            if self.applicant_name.isupper():
                return "%s" % self.applicant_name.title()
            return self.applicant_name
        return ""

    pretty_cooperator_name.short_description = "Cooperator name"

    def significant_dates(self):
        """
        Convenience method to display multiple dates in a single admin changelist column.
        """
        datelist_string = """<ul>
            <li>Start date: %s</li>
            <li>Expires: %s</li>
            </ul>""" % (
            self.proj_start_dt or "",
            self.proj_expiration_dt or "",
        )
        return mark_safe(datelist_string)

    significant_dates.allow_tags = True

    # TO-DO: Write save to write GID


class GrantAuthority(models.Model):
    grant = models.ForeignKey(Grant, on_delete=models.DO_NOTHING, db_column="grant_cn")
    authority_cd = models.CharField(max_length=40)
    authority_desc = models.CharField(
        "Authority Description", max_length=120, blank=True, null=True
    )
    last_update = models.DateField()

    class Meta:
        db_table = "ii_ga_authorities"
        verbose_name_plural = "Grant authorities"

    def __str__(self):
        return "%s: %s" % (self.authority_cd, self.grant)

    def pretty_str(self):
        return "%s: %s" % (self.authority_cd, self.grant.title())

    pretty_str.short_description = "Grant Authority"


class Note(models.Model):
    cn = models.CharField(primary_key=True, max_length=34)
    grant = models.ForeignKey(Grant, on_delete=models.DO_NOTHING, db_column="grant_cn")
    note_by = models.CharField(max_length=30)
    note_date = models.DateField()
    comments = models.CharField(max_length=2000)
    created_by = models.CharField(max_length=30)
    created_date = models.DateField()
    created_in_instance = models.DecimalField(max_digits=6, decimal_places=0)
    modified_by = models.CharField(max_length=30, blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    modified_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True
    )
    note_type = models.CharField(max_length=50, blank=True, null=True)
    email_to = models.CharField(max_length=500, blank=True, null=True)
    email_date = models.DateField(blank=True, null=True)
    last_update = models.DateField()

    def __str__(self):
        return " - ".join([self.comments[:80], str(self.grant)])

    class Meta:
        db_table = "ii_ga_notes"
