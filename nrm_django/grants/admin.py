from django.contrib import admin
from django.urls import path
from django.views.generic.list import ListView

from .forms import MinGrantForm
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
