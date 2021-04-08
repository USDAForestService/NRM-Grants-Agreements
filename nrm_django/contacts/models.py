# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from grants.models import Grant
from grants.choices import BOOL_CHOICES


class AccomplishmentInstrument(models.Model):
    cn = models.CharField(primary_key=True, max_length=34)
    grant = models.OneToOneField(Grant, to_field="gid",
            on_delete=models.CASCADE, db_column="id")
    name = models.CharField(max_length=200, blank=True, null=True)
    obj_tech = models.CharField(max_length=30)
    obj_name = models.CharField(max_length=30)
    obj_class = models.CharField(max_length=30)
    managing_cont_cn = models.CharField(max_length=34, blank=True, null=True)
    replaced_by_ai_cn = models.CharField(max_length=34, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    exp_expiration_date = models.DateField(blank=True, null=True)
    tim_allow_updates = models.CharField(max_length=1, blank=True, null=True)
    tim_contract_no = models.CharField(max_length=15, blank=True, null=True)
    tim_region = models.CharField(max_length=2, blank=True, null=True)
    tim_forest = models.CharField(max_length=2, blank=True, null=True)
    tim_district = models.CharField(max_length=2, blank=True, null=True)
    acbladd_bill_address_id = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    trans_id = models.CharField(max_length=34, blank=True, null=True)
    created_by = models.CharField(max_length=30)
    created_date = models.DateField()
    created_in_instance = models.DecimalField(max_digits=6, decimal_places=0)
    modified_by = models.CharField(max_length=30, blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    modified_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True
    )
    master_site = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True
    )
    security_id = models.CharField(max_length=30)
    agency_code = models.CharField(max_length=4, blank=True, null=True)
    parent_cn = models.CharField(max_length=34, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "accplishment_instruments"
        unique_together = (("obj_name", "id", "security_id", "trans_id"),)


class AdminUnit(models.Model):
    admin_unit_cn = models.CharField(max_length=40, primary_key=True)
    fs_unit_id = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    parent_unit_fk = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateField()

    class Meta:
        managed = False
        db_table = "admin_units"


class Contact(models.Model):
    cn = models.CharField(
        primary_key=True,
        max_length=34,
        editable=False,
    )
    id = models.CharField(
        "Contact ID",
        max_length=30,
        editable=False,
        help_text="""
            For new Contacts, this field is a system generated number.
            For older contacts it will be a shortened version of the contact's full name or organization title.
        """,
    )
    obj_tech = models.CharField(max_length=30, editable=False, default="ORACLE")
    obj_name = models.CharField(max_length=30, editable=False, default="ORGANIZATION")
    obj_class = models.CharField(max_length=30, editable=False, default="CONTACT")

    # TO-DO: Capture request.user on save()
    created_by = models.CharField(
        max_length=30, editable=False, help_text="Should capture username."
    )
    created_date = models.DateField(auto_now_add=True)
    # Need to capture the instance, when we have one.
    created_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, editable=False
    )
    trans_id = models.CharField("Trans ID", max_length=34, blank=True, null=True)
    # User guide says this is display only. Unclear how new values are created.
    # TO-DO: Find out how
    name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        editable=False,
        help_text="Contact's Last Name, First Name",
    )
    master_site = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True
    )
    remarks = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Any comments regarding the contact or cooperator.",
    )
    modified_by = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        editable=False,
        help_text="Should capture username.",
    )
    modified_date = models.DateField(blank=True, null=True, auto_now=True)
    modified_in_instance = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True, editable=False
    )
    security_id = models.CharField(max_length=30, blank=True, null=True, editable=False)
    agency_code = models.CharField(max_length=4)
    admin_org_ind = models.CharField("Admin Org", max_length=1, choices=BOOL_CHOICES)
    # ein and duns are noted as display only in the User Guide
    # TO-DO: determine how new entries can be created
    ein = models.CharField(
        "EIN",
        max_length=40,
        blank=True,
        null=True,
        editable=False,
        help_text="Employer Identification Number.",
    )
    duns = models.CharField(
        "DUNS",
        max_length=40,
        blank=True,
        null=True,
        editable=False,
        help_text="""
            The identification number assigned to the cooperator/recipient by the
            Dun and Bradstreet Data Universal Numbering System (DUNS).
            Call 1-866-705-5711 or visit the DUNS Number Request Form to request and register for a DUNS number.
        """,
    )
    faads_cn = models.CharField(max_length=34, blank=True, null=True, editable=False)
    ffis_vendor_status = models.CharField(
        "FFIS vendor status", max_length=40, blank=True, null=True
    )
    alc_code = models.CharField(
        "ALC",
        max_length=40,
        blank=True,
        null=True,
        help_text="The Agency Location Code.",
    )
    parent_duns = models.CharField(
        "Parent DUNS",
        max_length=40,
        blank=True,
        null=True,
        help_text="""
            The identification number assigned to the cooperator/recipient by the
            Dun and Bradstreet Data Universal Numbering System (DUNS).""",
    )
    # Choices
    duns_confidence_cd = models.CharField(
        "DUNS Confidence Score",
        max_length=2,
        blank=True,
        null=True,
        help_text="Confidence Code assigned via SAM validation.",
    )
    international = models.CharField(
        max_length=1, blank=True, null=True, default="N", choices=BOOL_CHOICES
    )
    archived_flag = models.CharField(max_length=1, default="N", choices=BOOL_CHOICES)
    office_hours = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ii_contacts"
        unique_together = (("obj_tech", "obj_name", "obj_class", "id", "trans_id"),)

    def __str__(self):
        return self.name


class AccinstContLink(models.Model):
    accinst = models.ForeignKey(
        AccomplishmentInstrument, models.DO_NOTHING, db_column="accinst_cn"
    )
    contact = models.ForeignKey(
        Contact, models.DO_NOTHING, db_column="cont_cn"
    )
    link_type_name = models.CharField(max_length=40)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    leading_ind = models.CharField(max_length=1, blank=True, null=True)
    department = models.CharField(max_length=40, blank=True, null=True)
    division = models.CharField(max_length=40, blank=True, null=True)
    # Choices
    ffis_vendor_id_pre_fmmi = models.CharField(
        "FMMI Vendor ID",
        max_length=11,
        blank=True,
        null=True,
        help_text="The cooperator/recipient's VEND number as assigned by FMMI.",
    )
    # TO-DO: Find out what this field is for
    faads_addr_cn = models.CharField(max_length=34, blank=True, null=True)
    # CHOICES
    institution_code = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        help_text="""
            The institution code for State Controlled Institution of Higher Learning only.
            Required if FFATA reported.
        """,
    )
    fed_debt_delnqnt_ind = models.CharField(
        "Delinquent on Fed. Debt",
        max_length=1,
        default="N",
        choices=BOOL_CHOICES,
        blank=True,
        null=True,
        help_text="""
            Check this box to indicate if the applicant is delinquent on any federal debt.
        """,
    )
    payee_ind = models.CharField(
        "Payee", max_length=1, blank=True, null=True, choices=BOOL_CHOICES, default="N"
    )
    applicant_ind = models.CharField(max_length=1, blank=True, null=True)
    link_sub_type = models.CharField(
        "Sub Type",
        max_length=40,
        blank=True,
        null=True,
        help_text="""
            Indicates the type of contact, for example, FS Signatory Official (SO) or Reviewer (RW),
            depending on the responsibility/role the contact has with the instrument.
        """,
    )
    cn = models.CharField(primary_key=True, max_length=34)
    ffis_can_number_status = models.CharField(max_length=40, blank=True, null=True)
    payer_ind = models.CharField(max_length=1, blank=True, null=True)
    fmmi_customer_number = models.CharField(max_length=10, blank=True, null=True)
    ffis_vendor_id = models.CharField(max_length=10, blank=True, null=True)
    fmmi_customer_number_status = models.CharField(max_length=40, blank=True, null=True)
    sam_expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ii_accinst_cont_links"
        unique_together = (
            ("accinst_cn", "cont_cn", "link_type_name", "link_sub_type"),
        )
