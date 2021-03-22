from django.contrib import admin
from django.urls import path
from django.views.generic.list import ListView

from .models import Grant, GrantAuthority, Note


class NoteInline(admin.TabularInline):
    model = Note


class GrantAuthorityInline(admin.TabularInline):
    model = GrantAuthority


class GrantAdmin(admin.ModelAdmin):
    inlines = [GrantAuthorityInline, NoteInline]
    list_display = (
        "pretty_name",
        "gid",
        "pretty_cooperator_name",
        "proj_start_dt",
        "proj_expiration_dt",
    )
    list_filter = ("status", "application_type")
    readonly_fields = [
        "gid",
        "created_date",
        "created_in_instance",
        "modified_date",
        "status_date",
    ]
    search_fields = [
        "proj_title",
        "proj_desc",
        "gid",
        "application_id",
        "applicant_name",
    ]
    fieldsets = (
        (
            "Required",
            {
                "fields": (
                    "proj_title",
                    ("application_type", "app_submission_type"),
                    ("app_submit_date", "app_received_date"),
                    ("proposed_start_date", "proposed_end_date"),
                    ("status", "status_date"),
                    (
                        "international_act_ind",
                        "advance_allowed_ind",
                        "aop_ind",
                    ),
                )
            },
        ),
        (
            "Project info",
            {
                "classes": ("collapse",),
                "fields": (
                    "proj_status",
                    "proj_desc",
                    (
                        "proj_received_dt",
                        "proj_execution_dt",
                        "proj_start_dt",
                        "proj_obligation_dt",
                    ),
                    ("proj_expiration_dt", "proj_close_dt", "proj_cancellation_dt"),
                    (
                        "proj_type",
                        "proj_cfda_no",
                        "project_congressional_district",
                    ),
                ),
            },
        ),
        (
            "Grant/Agreement",
            {
                "classes": ("collapse",),
                "fields": (
                    "comments",
                    ("date_mailed", "date_signed"),
                ),
            },
        ),
        (
            "Fed Info",
            {
                "classes": ("collapse",),
                "fields": (
                    ("fed_id_fy", "fed_id_type", "fed_id_agency", "fed_id_region"),
                    ("fed_id_unit", "fed_id_subunit", "fed_id_seq"),
                    ("orig_fed_id", "master_fed_id"),
                ),
            },
        ),
        (
            "State info",
            {
                "classes": ("collapse",),
                "fields": (
                    ("state_identifier", "state_eo_code", "state_eo_date"),
                    ("managing_state_county"),
                ),
            },
        ),
        (
            "EST Funds",
            {
                "classes": ("collapse",),
                "fields": (
                    "fed_est_fund",
                    "applicant_est_fund",
                    "state_est_fund",
                    "local_est_fund",
                    "pi_est_fund",
                    "oth_est_fund",
                ),
            },
        ),
        (
            "WPPP",
            {
                "classes": ("collapse",),
                "fields": ("wppp_status", "wppp_status_date"),
            },
        ),
        (
            "RWU",
            {
                "classes": ("collapse",),
                "fields": (
                    "proj_rwu",
                    "research_type",
                    "extramural_ind",
                    "proj_science_cd",
                    "journal_ind",
                ),
            },
        ),
        (
            "Other",
            {
                "classes": ("collapse",),
                "fields": (
                    "mod_number",
                    "geo_type",
                    "areas_effected",
                    "ffin",
                    "reroute_from",
                    "reroute_date",
                    "certificaion_date",
                    "ffis_doc_id",
                    "applicant_name",
                    "authority_approval",
                    "authority",
                    "format",
                    "other_approval",
                    "master_agreement_ind",
                    "progrm_responsibility_type",
                    "cooperator_agreement_number",
                    "admin_open",
                ),
            },
        ),
    )

    def get_urls(self):
        """
        Defines custom ADMIN urls.
        If you're looking for them in some urls.py, they're not there, they're here.
        """
        urls = super().get_urls()
        my_urls = [
            path(
                "<username>/items/",
                self.admin_site.admin_view(UserItemsView.as_view()),
                name="user_items",
            ),
        ]
        return my_urls + urls


class GrantAuthorityAdmin(admin.ModelAdmin):
    list_filter = ("authority_cd",)


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "note_date",
        "comments",
        "note_by",
        "grant",
    )


class UserItemsView(ListView):

    template_name = "admin/user_items.html"

    def get_queryset(self):
        return Grant.objects.filter(created_by=self.kwargs.get("username")).order_by(
            "-status_date"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context


admin.site.register(Grant, GrantAdmin)
admin.site.register(GrantAuthority, GrantAuthorityAdmin)
admin.site.register(Note, NoteAdmin)
