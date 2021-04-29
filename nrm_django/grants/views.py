from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .forms import GrantForm
from .models import Grant


class GrantCreateView(LoginRequiredMixin, CreateView):
    model = Grant
    form_class = GrantForm
    login_url = "/admin/"
    template_name = "grants/create.html"

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
