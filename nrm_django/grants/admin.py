from django.contrib import admin

from .models import Grant, GrantAuthority, Note


class GrantAdmin(admin.ModelAdmin):
    # list options
    list_display = (
        "resolved_id",
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


admin.site.register(Grant, GrantAdmin)
admin.site.register(GrantAuthority, GrantAuthorityAdmin)
admin.site.register(Note, NoteAdmin)
