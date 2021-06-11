from django import template

from django.contrib.admin.templatetags.admin_list import search_form
from django.contrib.admin.templatetags.base import InclusionAdminNode

register = template.Library()


def this_search_form(cl, description):
    orig = search_form(cl)
    orig["search_description"] = description
    return orig


@register.tag(name="search_form")
def search_form_with_description_tag(parser, token):
    """
    Duplicates the search_form template tag from django.contrib.admin.templatetags

    But with a description that can be passed in.
    """
    return InclusionAdminNode(
        parser,
        token,
        func=this_search_form,
        template_name="search_form.html",
        takes_context=False,
    )
