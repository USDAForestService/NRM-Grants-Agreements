from urllib.parse import quote, urljoin

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def uswds_static(filepath):
    """
    Essentially duplicates the Django static template tag
    to build in the path to the current USWDS version, as defined in settings.
    You'll call it more or less just like calling static:
    Example: "{% uswds_static 'path/to/uswds/file' %}
    """
    uswds_fullpath = settings.STATIC_URL + settings.USWDS_PATH
    return urljoin(uswds_fullpath, quote(filepath))
