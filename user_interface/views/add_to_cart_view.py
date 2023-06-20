import json

from django.http import HttpRequest, JsonResponse

from user_interface.models import Cart, ProductParameterValue


def add_to_cart_view(request: HttpRequest) -> JsonResponse:
    """Add or update cart model."""
    request_data = json.loads(request.body.decode("utf-8"))

    product_slug = request_data["product_slug"]
    product_parameter_value = request_data["product_parameter_value"]
    user = request.user

    product_parameter_value = ProductParameterValue.objects.get(
        value=product_parameter_value, product__slug=product_slug
    )
    cart, _ = Cart.objects.get_or_create(user=user)
    cart.products.add(product_parameter_value)
    cart.save()

    return JsonResponse({"cart": cart.pk})
