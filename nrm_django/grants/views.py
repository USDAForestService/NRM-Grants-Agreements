import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import MinGrantForm, GrantUpdateForm
from .models import Grant


def run_save_checks(form, request):
    """
    Every time a Grant object is saved, regardless of which form is submitted,
    there are several things that we need to check and determine if they're revised or not.
    We'll capture them here, then call this in form_valid()
    """
    new_status = None
    # Do stuff here to determine if status should change, and if so, change it.

    if new_status:
        # form.instance.status = new_status  # to-do: update this to reflect the real check
        form.instance.status_date = datetime.datetime.now()

    # TO-DO: Have a proper FK to a user object for modified_by,
    # so we can link to the user and not a str representation.
    form.instance.modified_by = str(request.user)
    return form


class GrantCreateView(LoginRequiredMixin, CreateView):
    model = Grant
    form_class = MinGrantForm
    login_url = "/admin/"
    template_name = "grants/create.html"

    def get_context_data(self, **kwargs):
        """
        In order to duplicate Admin functionality and not make our pages blow up in interesting ways,
        we're going to have to add some things to context ourselves.
        We should track these carefully, since we may be able to remove some
        if they're not used in our custom change_form.html
        """
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "opts": Grant._meta,
                "is_popup": False,  # needed by admin/base.html
                "save_as": False,
                "has_delete_permission": False,
                "has_add_permission": False,
                "has_change_permission": False,
                "has_view_permission": True,
                "has_editable_inline_admin_formsets": True,
                "add": True,
                "change": False,
            }
        )
        return context

    def form_valid(self, form):
        form = run_save_checks(form, self.request)
        return super().form_valid(form)


class GrantUpdateView(LoginRequiredMixin, UpdateView):
    model = Grant
    form_class = GrantUpdateForm
    login_url = "/admin/"
    template_name = "grants/update.html"

    def get_context_data(self, **kwargs):
        """
        In order to duplicate Admin functionality, we're going to have to add some things to context ourselves.
        We should track these carefully, since we may be able to remove some if they're not used in our custom change_form.html
        """
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "opts": Grant._meta,
                "is_popup": False,  # needed by admin/base.html
                "save_as": False,
                "has_delete_permission": False,
                "has_add_permission": False,
                "has_change_permission": False,
                "has_view_permission": True,
                "has_editable_inline_admin_formsets": True,
                "add": True,
                "change": False,
            }
        )
        return context

    def form_valid(self, form):
        form = run_save_checks(form, self.request)
        return super().form_valid(form)


class GrantDetailView(LoginRequiredMixin, DetailView):
    model = Grant


class UserItemsView(LoginRequiredMixin, ListView):
    template_name = "admin/user_items.html"

    def get_queryset(self):
        return Grant.objects.filter(created_by=self.kwargs.get("username")).order_by(
            "-status_date"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context
