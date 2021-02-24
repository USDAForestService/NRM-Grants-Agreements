from django.db import models


class Grants(models.Model):
    """
    Defines a grant and it's status through the full workflow.

    Has a lot of related info in here, too.
    """
    cn = models.CharField(max_length=34)
    proj_title = models.CharField("Project title", max_length=200)
    proj_status = models.CharField("Project status", max_length=15, blank=True, null=True) # choices????
    application_id = models.CharField(max_length=34)
    application_type = models.CharField(max_length=30)
    app_submission_type = models.CharField("Application submission type", max_length=100) # choices???
    app_submit_date = models.DateField("Application submitted")
    app_received_date = models.DateField("Application received")
    hhs_payment_ind = models.CharField(max_length=1) # Y/N indicator, Probably boolean
    # grant status and significant dates (I think)
    proposed_start_date = models.DateField()
    proposed_end_date = models.DateField()
    locked_ind = models.CharField(max_length=1) #Y/N indicator, Probably boolean
    status = models.CharField(max_length=40)
    status_date = models.DateField()
    created_by = models.CharField(max_length=30) # FK?
    created_date = models.DateField()
    created_in_instance = models.DecimalField(max_digits=6, decimal_places=0)  # Hmmm. What is instance here (and elsewhere)?
    modified_by = models.CharField(max_length=30, blank=True, null=True)       # FK?
    modified_date = models.DateField(blank=True, null=True)                    # First modified? Last modified?
    modified_in_instance = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    # Fields for Fed ID. What's that?
    fed_id_fy = models.CharField(max_length=4, blank=True, null=True)          # what's fed_id? what's fy?
    fed_id_type = models.CharField(max_length=2, blank=True, null=True)
    fed_id_agency = models.CharField(max_length=2, blank=True, null=True)
    fed_id_region = models.CharField(max_length=2, blank=True, null=True)
    fed_id_unit = models.CharField(max_length=2, blank=True, null=True)
    fed_id_subunit = models.CharField(max_length=2, blank=True, null=True)
    fed_id_seq = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    
    # Fields describing project(s) and significant dates.
    proj_desc = models.CharField("Project description", max_length=2000, blank=True, null=True)
    proj_received_dt = models.DateField("Project received date", blank=True, null=True)
    proj_execution_dt = models.DateField("Project execution date", blank=True, null=True)
    proj_start_dt = models.DateField("Project start date", blank=True, null=True)
    proj_obligation_dt = models.DateField("Project obligation date", blank=True, null=True)
    proj_expiration_dt = models.DateField("Project expiration date", blank=True, null=True)
    proj_rwu = models.CharField(max_length=10, blank=True, null=True)   # What's RWU
    proj_close_dt = models.DateField("Project close date", blank=True, null=True)
    proj_cancellation_dt = models.DateField("Project cancellation date", blank=True, null=True)
    proj_cfda_no = models.CharField("Project CFDA", max_length=40, blank=True, null=True)
    proj_science_cd = models.CharField(max_length=3, blank=True, null=True) # What's science CD?
    project_congressional_district = models.CharField(max_length=40, blank=True, null=True)
    date_mailed = models.DateField(blank=True, null=True)
    date_signed = models.DateField(blank=True, null=True)
    extramural_ind = models.CharField(max_length=1, blank=True, null=True) # Y/N indicator, Probably boolean
    research_type = models.CharField(max_length=1, blank=True, null=True)
    journal_ind = models.CharField(max_length=1, blank=True, null=True) # Y/N indicator, Probably boolean
    mod_number = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    orig_fed_id = models.CharField(max_length=120, blank=True, null=True)
    comments = models.CharField(max_length=2000, blank=True, null=True)
    master_fed_id = models.CharField(max_length=120, blank=True, null=True)
    aop_ind = models.CharField(max_length=1, blank=True, null=True)
    geo_type = models.CharField(max_length=2, blank=True, null=True)
    managing_state_county = models.CharField(max_length=240, blank=True, null=True)
    areas_effected = models.CharField(max_length=200, blank=True, null=True)
    ffin = models.CharField(max_length=40, blank=True, null=True)
    state_identifier = models.CharField(max_length=40, blank=True, null=True) # choices? FK?
    state_eo_code = models.CharField(max_length=1, blank=True, null=True)
    state_eo_date = models.DateField(blank=True, null=True)
    fed_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    applicant_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    state_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    local_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pi_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    oth_est_fund = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reroute_from = models.CharField(max_length=10, blank=True, null=True)
    reroute_date = models.DateField(blank=True, null=True)
    certificaion_date = models.DateField(blank=True, null=True)
    ffis_doc_id = models.CharField(max_length=11, blank=True, null=True)
    applicant_name = models.CharField(max_length=200, blank=True, null=True)
    international_act_ind = models.CharField(max_length=1, blank=True, null=True) # Boolean indicator?
    proj_type = models.CharField(max_length=3, blank=True, null=True) # Choices? FK?
    advance_allowed_ind = models.CharField('Advance Allowed', max_length=1, blank=True, null=True) # Y/N indicator, Probably boolean
    authority_approval = models.CharField(max_length=1, blank=True, null=True) # probably boolean
    authority = models.CharField(max_length=1, blank=True, null=True) # probably boolean. Maybe FK
    format = models.CharField(max_length=1, blank=True, null=True) # we'll need to safely rename this column
    other_approval = models.CharField(max_length=1, blank=True, null=True)
    master_agreement_ind = models.CharField(max_length=1, blank=True, null=True) # boolean indicator
    progrm_responsibility_type = models.CharField(max_length=30, blank=True, null=True) # choices?
    # What is wppp?
    wppp_status = models.CharField(max_length=40, blank=True, null=True)
    wppp_status_date = models.DateField(blank=True, null=True)
    cooperator_agreement_number = models.CharField(max_length=34, blank=True, null=True) # Is this used to key to a cooperator agreement?
    gid = models.CharField(max_length=16, blank=True, null=True)  # FK, or is this the grant PK?
    admin_open = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField() # last update for what? The Grant? Should this be user-editable?

    class Meta:
        managed = False
        db_table = 'ii_grants'