from django import template


register = template.Library()


@register.filter(name="dict_key")
def dict_key(dict: dict, key: str):
    """Return value of dict."""
    return dict[key]
