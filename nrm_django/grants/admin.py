from django.contrib import admin
from django.urls import path
from django.views.generic.list import ListView

from .forms import GrantForm
from .models import Grant, GrantAuthority, Note


class NoteInline(admin.TabularInline):
    model = Note


class GrantAuthorityInline(admin.TabularInline):
    model = GrantAuthority


class GrantAdmin(admin.ModelAdmin):
    # list options
    list_display = (
        "gid",
        "pretty_cooperator_name",
        "pretty_name",
        "proj_start_dt",
        "proj_expiration_dt",
    )
    list_filter = ("status", "application_type")
    search_fields = [
        "proj_title",
        "proj_desc",
        "gid",
        "application_id",
        "applicant_name",
    ]
    # detail options
    inlines = [GrantAuthorityInline, NoteInline]

    fieldsets = []

    def change_view(self, request, object_id, extra_context=None):
        """
        In a change/update view, we'll want a lot more fields and fieldsets,
        so we'll append to the base list of required fields.
        """
        self.fieldsets += [
            (
                "Details",
                {
                    "fields": (
                        ("gid",),
                        ("proj_desc", "areas_effected"),
                        ("cooperator_agreement_number", "extramural_ind"),
                        ("comments",),
                        (
                            "international_act_ind",
                            "advance_allowed_ind",
                            "aop_ind",
                        ),
                    )
                },
            ),
            (
                "RWU",
                {
                    "classes": ("collapse",),
                    "fields": (
                        "proj_rwu",
                        ("research_type", "journal_ind"),
                    ),
                },
            ),
            (
                "Project info",
                {
                    "classes": ("collapse",),
                    "fields": (
                        ("proj_type", "proj_status"),
                        ("proj_science_cd", "project_congressional_district"),
                        ("proj_received_dt", "proj_execution_dt"),
                        ("proj_start_dt", "proj_obligation_dt"),
                        ("proj_expiration_dt", "proj_close_dt", "proj_cancellation_dt"),
                    ),
                },
            ),
            (
                "Grant/Agreement",
                {
                    "classes": ("collapse",),
                    "fields": (("date_mailed", "date_signed"),),
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
                        ("state_identifier",),
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
                "Other",
                {
                    "classes": ("collapse",),
                    "fields": (
                        "mod_number",
                        "geo_type",
                        "ffin",
                        "reroute_from",
                        "reroute_date",
                        "certificaion_date",
                        "ffis_doc_id",
                        "authority_approval",
                        "authority",
                        "format",
                        "other_approval",
                        "admin_open",
                    ),
                },
            ),
        ]
        return super(GrantAdmin, self).change_view(request, object_id)

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
    # Grants is too big to be in a selectbox.
    # As long as Notes aren't stricly inlines, we're gonna need to do something.
    # This is one possible something.
    raw_id_fields = ("grant",)


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
