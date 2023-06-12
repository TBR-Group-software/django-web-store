from django import template
from django.templatetags.static import static

from user_interface.models import ProductImage

register = template.Library()


@register.filter
def get_product_image_url(product_id: int) -> ProductImage | str:
    """Return url of main image of product."""
    try:
        main_image = ProductImage.objects.get(product__id=product_id, image_type="MAIN")
    except ProductImage.DoesNotExist:
        return static("img/product/none_image.jpg")
    return main_image
