from django import template
from django.templatetags.static import static

from product.models import ProductImage


register = template.Library()


@register.filter
def get_product_image_url(
    product_id: int, content_type: str = "product"
) -> ProductImage | str:
    """Return url of main image of product."""
    try:
        main_image = ProductImage.objects.get(
            object_id=product_id, image_type="MAIN", content_type__model=content_type
        )
    except ProductImage.DoesNotExist:
        return static("img/product/none_image.jpg")
    return main_image
