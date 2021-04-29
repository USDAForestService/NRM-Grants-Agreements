from django.db import models
from django.utils.safestring import mark_safe
from django.utils.functional import cached_property

from .choices import (
    AB_CHOICES,
    APPLICATION_TYPE_CHOICES,
    APP_SUBMISSION_TYPE_CHOICES,
    BOOL_CHOICES,
    CFDA_CHOICES,
    FED_ID_REGION_CHOICES,
    FED_ID_TYPE_CHOICES,
    NOTE_TYPE_CHOICES,
    PROGRAM_RESPONSIBILITY_TYPE_CHOICES,
    RESEARCH_TYPE_CHOICES,
    RWU_CHOICES,
    SCIENCE_CODE_CHOICES,
    STATUS_CHOICES,
    WPAP_STATUS_CHOICES,
    YEAR_CHOICES,
)
from contacts.models import AccomplishmentInstrument


class Grant(models.Model):
    """
    Defines a grant and it's status through the full workflow.

    Has a lot of related info in here, too.
    """

    # CN may need to be viewable at some times, per the User Guide.
    # Unclear what the use case might be, though.
    # Per Jamie, it is a random number, but the first part is based on FY generated and org...
    # so 2109**** would be from region 09
    cn = models.CharField(
        "Proposal ID",
        max_length=34,
        primary_key=True,
        editable=False,
        db_index=True,
        help_text="A system-generated number used to identify the proposal before an agreement number is assigned or the instrument is executed.",
    )
    proj_title = models.CharField(
        "Project title",
        max_length=200,
        db_index=True,
        help_text="The short and concise name of the project. Do not include any acronyms, unit codes, or funding codes.",
    )
    proj_status = models.CharField(
        "Project status",
        max_length=15,
        blank=True,
        null=True,
        choices=AB_CHOICES,
        help_text="The Status of the grant or agreement (instrument).",
    )
    # Sys-generated, once initial proposal saved. Control number.
    # Older field, not user viewable. Only used for historical records.
    application_id = models.CharField(max_length=34, editable=False)
    application_type = models.CharField(
        "Type of application",
        max_length=30,
        choices=APPLICATION_TYPE_CHOICES,
        help_text="""
            Applies to instruments with Federal Financial Assistance (FFA).
            Select OTHER if not FFA.
        """,
    )
    app_submission_type = models.CharField(
        "Type of Submission",
        max_length=100,
        choices=APP_SUBMISSION_TYPE_CHOICES,
        help_text="""
            Applies to instruments with Federal Financial Assistance (FFA).
            Select OTHER if not FFA.
        """,
    )
    app_submit_date = models.DateField(
        "Application submitted",
        help_text="The date the proposal was submitted for review or processing.",
    )
    app_received_date = models.DateField(
        "Application received",
        help_text="The date the proposal was received by the Forest Service.",
    )
    # No longer utilized, not in the application.
    hhs_payment_ind = models.CharField(
        max_length=1,
        default="N",
        editable=False,
        help_text="Was only used by NRS (Northern Research Station) and NA Northeastern Area (S&PF).",
    )

    proposed_start_date = models.DateField(
        help_text="""
            The date the project is expected to start as negotiated in the agreement.
            This date cannot be after the Expiration date.
        """
    )
    proposed_end_date = models.DateField(
        help_text="""The date the project is expected to end as negotiated in the agreement."""
    )

    # locked_ind was never implemented in the front end.
    # The desire is that sys admins and help desk should be able to lock a record
    # so it cannot be edited (unless they unlock it).
    # For now, marking it as not-editable.
    locked_ind = models.CharField(
        choices=BOOL_CHOICES, max_length=1, default="N", editable=False
    )
    status = models.CharField(
        "Agreement Status",
        max_length=40,
        choices=STATUS_CHOICES,
        default="NEW-APPLICATION",
        editable=False,
    )
    status_date = models.DateField(auto_now_add=True)
    # TO-DO: created_by should record current user on save()
    created_by = models.CharField(max_length=30, editable=False)  # FK?
    created_date = models.DateField(auto_now_add=True)
    # Sys generated field. Comes from RACA, says what instance of the application it is.
    # TO-DO: determine how to generate it.
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
    fed_id_agency = models.CharField(
        "Agency",
        max_length=2,
        blank=True,
        null=True,
        help_text="""
            The two-digit code the agency.
            For the Forest Service, the agency is always "11".
            """,
        default="11",
    )
    fed_id_region = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        choices=FED_ID_REGION_CHOICES,
        help_text="The two-digit code for the region of the instrument, such as 01 or 13.",
    )
    fed_id_unit = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        help_text="The two-digit code for the unit.",
    )
    fed_id_subunit = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        help_text="The two-digit code for the subunit.",
    )
    fed_id_seq = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        blank=True,
        null=True,
        help_text="The three-digit code for the sequence number of the instrument.",
    )

    # Fields describing project(s) and significant dates.
    proj_type = models.CharField(
        "Project Type", max_length=3, blank=True, null=True, choices=AB_CHOICES
    )
    proj_desc = models.TextField(
        "Project description",
        max_length=2000,
        blank=True,
        null=True,
        help_text="Narrative text describing the project.",
    )
    proj_received_dt = models.DateField(
        "Project received date",
        blank=True,
        null=True,
        help_text="The date the State received the proposal for consideration.",
    )
    proj_execution_dt = models.DateField(
        "Project execution date", blank=True, null=True
    )
    proj_start_dt = models.DateField(
        "Start date", blank=True, null=True, help_text=""""""
    )
    proj_obligation_dt = models.DateField(
        "Project obligation date", blank=True, null=True
    )
    proj_expiration_dt = models.DateField("Expires", blank=True, null=True)

    proj_close_dt = models.DateField(
        "Close date",
        blank=True,
        null=True,
        help_text="""
            The date the instrument is closed.
            Denotes the grant or agreement has been executed and has been officially closed.
            Required when closing the instrument.
        """,
    )
    proj_cancellation_dt = models.DateField(
        "Cancellation date",
        blank=True,
        null=True,
        help_text="The date the instrument is canceled.",
    )
    proj_rwu = models.CharField(
        "Research Work Unit",
        max_length=10,
        blank=True,
        null=True,
        choices=RWU_CHOICES,
    )
    proj_cfda_no = models.CharField(
        "CFDA Number",
        max_length=40,
        blank=True,
        null=True,
        choices=CFDA_CHOICES,
        help_text="""
            The Catalog of Federal Domestic Assistance (CFDA) Number.
            Required if the instrument was issued under a federal financial assistance authority
            (instrument type DG and CA only). REQUIRED FOR APPROVAL""",
    )
    proj_science_cd = models.CharField(
        "Science Code",
        max_length=3,
        blank=True,
        null=True,
        choices=SCIENCE_CODE_CHOICES,
    )
    project_congressional_district = models.CharField(
        max_length=40, blank=True, null=True
    )

    date_mailed = models.DateField(blank=True, null=True)
    date_signed = models.DateField(blank=True, null=True)
    comments = models.TextField(max_length=2000, blank=True, null=True)
    # Per user guide extramural_ind should be represented as a boolean
    # TO-DO: present it as a boolean (may require migrationi)
    extramural_ind = models.CharField(
        "Extramural",
        choices=BOOL_CHOICES,
        max_length=1,
        null=True,
        default="N",
        help_text="For reporting FS Research agreement activities only.",
    )  # should be a boolean, but appears to be null in some DB instances
    research_type = models.CharField(
        max_length=1, blank=True, null=True, choices=RESEARCH_TYPE_CHOICES
    )
    journal_ind = models.CharField("Journal", max_length=1, blank=True, null=True)
    mod_number = models.DecimalField(
        max_digits=3, decimal_places=0, blank=True, null=True
    )
    orig_fed_id = models.CharField(
        "Original Agreement Number",
        max_length=120,
        blank=True,
        null=True,
        help_text="""
            If there was a previous agreement, (prior to FY2000 numbering scheme),
            enter the original Forest Service identification number here to supply
            a cross-reference to the new agreement number.
            Note: Do not enter other agency agreement numbers in this field.
            They can be entered in the Comments field.
        """,
    )
    master_fed_id = models.CharField(
        "Master Fed ID", max_length=120, blank=True, null=True
    )
    aop_ind = models.CharField(
        "AOP",
        choices=BOOL_CHOICES,
        max_length=1,
        null=True,
        default="N",
        help_text="""
            Select Yes from the choice list if the instrument requires an Annual Operating Plan (AOP).
        """,
    )
    geo_type = models.CharField(max_length=2, blank=True, null=True)
    managing_state_county = models.CharField(max_length=240, blank=True, null=True)
    areas_effected = models.CharField(
        "Areas Affected",
        max_length=200,
        blank=True,
        null=True,
        help_text="""
            Areas (states, localities, congressional districts, and other areas) that are affected by the project.
        """,
    )
    ffis_doc_id = models.CharField("FFIS Doc", max_length=11, blank=True, null=True)
    ffin = models.CharField(
        "FMMI Agreement Number",
        max_length=40,
        blank=True,
        null=True,
        help_text="The agreement number assigned to the instrument in FMMI.",
    )

    # State fields
    state_identifier = models.CharField(
        max_length=40, blank=True, null=True
    )  # choices? FK?
    state_eo_code = models.CharField(
        "Subject to State E.O.",
        max_length=1,
        blank=True,
        null=True,
        choices=BOOL_CHOICES,
        default="N",
        help_text="Is this instrument subject to Executive Order 12372 review?",
    )
    # We validate on save that a date was entered if state_eo_code is Y
    state_eo_date = models.DateField(
        "EO Date",
        blank=True,
        null=True,
        help_text="""
            Executive Order 12372 review date.
            You must select a date if 'Subject to State E.O.' is Yes.""",
    )

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
    applicant_name = models.CharField("Applicant/Cooperator Name", max_length=200)
    international_act_ind = models.CharField(
        "International Activities",
        choices=BOOL_CHOICES,
        max_length=1,
        null=True,
        default="N",
        help_text="Indicates if the project has any associated international activities.",
    )
    advance_allowed_ind = models.CharField(
        "Advance Allowed",
        choices=BOOL_CHOICES,
        max_length=1,
        null=True,
        default="N",
        help_text="Indicates if advanced payments are allowed in the instrument. Select Y if advanced payments are allowed.",
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
    # Per User Guide, this field is not available until the instrument's status is PROP-ACCEPTED
    # TO-DO: Add runtime check for self.status and update form to make this editable if needed.
    master_agreement_ind = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        editable=False,
        choices=BOOL_CHOICES,
        default="N",
        help_text="Indicates if the instrument is a Master Agreement.",
    )
    progrm_responsibility_type = models.CharField(
        "Program Responsibility Type",
        max_length=30,
        choices=PROGRAM_RESPONSIBILITY_TYPE_CHOICES,
        help_text="""
            Indicates the specific responsibilities notification type
            (Incoming Funding, Outgoing Funding, or Non-Cash ie no exchange of funding)
            that is send to the Program Manager when the agreement is executed.
        """,
    )
    wppp_status = models.CharField(
        "WPAP Status",
        max_length=40,
        blank=True,
        null=True,
        choices=WPAP_STATUS_CHOICES,
        editable=False,
    )
    wppp_status_date = models.DateField(
        "WPAP status date", blank=True, null=True, editable=False
    )
    cooperator_agreement_number = models.CharField(
        max_length=34,
        blank=True,
        null=True,
        help_text="Cooperator's agreement number, if different than the Forest Service Agreement Number",
    )  # Is this used to key to a cooperator agreement?
    gid = models.CharField("Agreement Number", max_length=16, blank=True, null=True)
    admin_open = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(auto_now=True)

    class Meta:
        db_table = "ii_grants"
        verbose_name = "Grant/Agreement"
        verbose_name_plural = "Grants and Agreements"
        ordering = ["-created_date"]
        constraints = [models.UniqueConstraint(fields=["gid"], name="unique_gid")]

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

    @cached_property
    def contacts(self):
        """
        Follow the contact links and return a list of all the associated contacts."""
        try:
            instrument = self.accomplishmentinstrument
        except AccomplishmentInstrument.DoesNotExist:
            return []
        links = instrument.accinstcontlink_set.all()
        return [
            {
                "type": link.link_type_name,
                "sub_type": link.link_sub_type,
                "contact": link.contact,
            }
            for link in links
        ]

    @cached_property
    def org(self):
        """
        Shorthand accessor for the Organization code and name.
        Note that because of the lack of database integrity we can't trust it to be a true 1:1 relationship.
        Until that is cleared up we're going to have to use filter() because get() returns multiple and throws an error.
        We'll then grab the first from the set, believing the remainder are duplicates anyway.
        This is not ideal.
        """
        instrument = AccomplishmentInstrument.objects.filter(grant=self).first()
        if not instrument:
            return None
        return instrument.managing_contact


class GrantAuthority(models.Model):
    """
    Defines the authority a given Grant can use.

    This is one of the few models with a Django-generated PK.
    18F has a copy of possible authority_cd values at
    https://docs.google.com/document/d/1ngFEuIN5rtF-zx3WiIxnp31KWTtBmOMV/edit#heading=h.2kicxvv
    """

    grant = models.ForeignKey(
        Grant, on_delete=models.DO_NOTHING, db_column="grant_cn", editable=False
    )
    authority_cd = models.CharField(
        "Code",
        max_length=40,
        help_text="""
            The legislative authority code under which the instrument was authorized.
            The full list is in the GA User Guide""",
    )
    authority_desc = models.CharField(
        "Authority Description", max_length=120, blank=True, null=True
    )
    last_update = models.DateField(auto_now=True)

    class Meta:
        db_table = "ii_ga_authorities"
        verbose_name_plural = "Grant authorities"

    def __str__(self):
        return "%s: %s" % (self.authority_cd, self.grant)

    def pretty_str(self):
        return "%s: %s" % (self.authority_cd, self.grant.title())

    pretty_str.short_description = "Grant Authority"


class Note(models.Model):
    """
    Defines a note object, which describes a grant.
    """

    cn = models.CharField(
        primary_key=True, max_length=34, db_index=True, editable=False
    )
    grant = models.ForeignKey(Grant, on_delete=models.DO_NOTHING, db_column="grant_cn")
    comments = models.CharField(
        max_length=2000, help_text="Any additional comments regarding the project."
    )
    note_type = models.CharField(
        max_length=50, blank=True, null=True, choices=NOTE_TYPE_CHOICES
    )
    # we need to learn the difference between these two fields
    # and the _by fields need to update on save()
    note_by = models.CharField(
        max_length=30,
        editable=False,
        help_text="The user ID of the person who created the note.",
    )
    created_by = models.CharField(
        max_length=30,
        editable=False,
    )
    note_date = models.DateField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)

    # Needs to populate on save.
    modified_by = models.CharField(max_length=30, blank=True, null=True, editable=False)
    modified_date = models.DateField(blank=True, null=True, auto_now=True)
    last_update = models.DateField(auto_now=True)
    created_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, editable=False
    )
    modified_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True, editable=False
    )
    # we need to learn more about how exactly these email fields are used,
    # but per the User Guide they should not be user-editable.
    email_to = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        editable=False,
        help_text="The e-mail address(es) of the note recipient (if the message was sent to via e-mail).",
    )
    # The user guide indicates that email_date should be updated automatically after an email action takes place. Maybe.
    email_date = models.DateField(
        blank=True,
        null=True,
        editable=False,
        help_text="The date the note was sent to the e-mail recipient(s).",
    )

    def __str__(self):
        return " - ".join([self.comments[:80], str(self.grant)])

    class Meta:
        db_table = "ii_ga_notes"

    # TO-DO: custom save?
    # * Create CN


class Category(models.Model):
    cn = models.CharField(primary_key=True, max_length=34)
    grant = models.ForeignKey(Grant, models.DO_NOTHING, db_column="grant_cn")
    category_cd = models.CharField("Code", max_length=2)
    category_desc = models.CharField(
        "Description", max_length=120, blank=True, null=True
    )
    last_update = models.DateField(auto_now=True)

    class Meta:
        managed = False
        db_table = "ii_ga_ip_categories"

    def __str__(self):
        return self.category_desc
