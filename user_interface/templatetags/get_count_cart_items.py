from django.contrib.auth.models import User
from django import template

from cart.models import Cart


register = template.Library()


@register.filter(name="get_count_cart_items")
def get_count_cart_items(user: User) -> int:
    """Return count of items in cart of user."""
    return Cart.objects.get(user=user).products.all().count()
