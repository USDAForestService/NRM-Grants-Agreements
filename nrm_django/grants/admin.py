from django.contrib import admin
from django.urls import path
from django.views.generic.list import ListView

from .models import Grant, GrantAuthority, Note


class NoteInline(admin.TabularInline):
    model=Note


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "note_date",
        "comments",
        "note_by",
        "grant",
    )

class GrantAdmin(admin.ModelAdmin):
    inlines = [NoteInline]
    list_display = (
        "proj_title",
        "application_id",
        "application_type",
        "status",
        "app_submit_date",
        "app_received_date",
        "proposed_start_date",
    )
    list_filter = ("status",)
    readonly_fields = [
        "created_date",
        "created_in_instance",
        "modified_date",
        "status_date",
    ]
    search_fields = ["proj_title", "proj_desc", "application_id"]
    # list_editable = ['status',]
    fieldsets = (
        (
            "Project info",
            {
                "fields": (
                    "proj_title",
                    "proj_status",
                    "proj_desc",
                    (
                        "proj_received_dt",
                        "proj_execution_dt",
                        "proj_start_dt",
                        "proj_obligation_dt",
                    ),
                    ("proj_expiration_dt", "proj_close_dt", "proj_cancellation_dt"),
                )
            },
        ),
        (
            "Project info (Advanced)",
            {
                "classes": ("collapse",),
                "fields": (
                    (
                        "proj_rwu",
                        "proj_cfda_no",
                        "proj_science_cd",
                        "project_congressional_district",
                    )
                ),
            },
        ),
        (
            "Application",
            {
                "fields": (
                    ("application_id", "application_type", "app_submission_type"),
                    (
                        "app_submit_date",
                        "app_received_date",
                    ),
                ),
            },
        ),
        (
            "Grant",
            {
                "fields": (
                    "proposed_start_date",
                    "proposed_end_date",
                    "locked_ind",
                    ("status", "status_date"),
                    ("created_by", "created_date", "created_in_instance"),
                    ("modified_by", "modified_date", "modified_in_instance"),
                ),
            },
        ),
        (
            "Fed ID",
            {
                "classes": ("collapse",),
                "fields": (
                    ("fed_id_fy", "fed_id_type", "fed_id_agency", "fed_id_region"),
                    ("fed_id_unit", "fed_id_subunit", "fed_id_seq"),
                ),
            },
        ),
        (
            "Other",
            {
                "fields": (
                    "hhs_payment_ind",
                    "date_mailed",
                    "date_signed",
                    "extramural_ind",
                    "research_type",
                    "journal_ind",
                    "mod_number",
                    "orig_fed_id",
                    "comments",
                    "master_fed_id",
                    "aop_ind",
                    "geo_type",
                    "managing_state_county",
                    "areas_effected",
                    "ffin",
                    "state_identifier",
                    "state_eo_code",
                    "state_eo_date",
                    "fed_est_fund",
                    "applicant_est_fund",
                    "state_est_fund",
                    "local_est_fund",
                    "pi_est_fund",
                    "oth_est_fund",
                    "reroute_from",
                    "reroute_date",
                    "certificaion_date",
                    "ffis_doc_id",
                    "applicant_name",
                    "international_act_ind",
                    "proj_type",
                    "advance_allowed_ind",
                    "authority_approval",
                    "authority",
                    "format",
                    "other_approval",
                    "master_agreement_ind",
                    "progrm_responsibility_type",
                    "wppp_status",
                    "wppp_status_date",
                    "cooperator_agreement_number",
                    "admin_open",
                    "last_update",
                )
            },
        ),
    )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "my_view/<username>", self.admin_site.admin_view(CustomView.as_view())
            ),
        ]
        return my_urls + urls


class CustomView(ListView):

    template_name = "grants/index.html"

    def get_queryset(self):
        return (
            Grant.objects.filter(created_by=self.kwargs.get("username"))
            .values("cn", "proj_title", "status")
            .order_by("-status_date")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context


admin.site.register(Grant, GrantAdmin)
admin.site.register(GrantAuthority)
admin.site.register(Note, NoteAdmin)
