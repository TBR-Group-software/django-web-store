import json

from django.http import HttpRequest, JsonResponse

from user_interface.models import Cart, ProductParameterValue, CartAmmountProduct


def edit_cart_view(request: HttpRequest) -> JsonResponse:
    """Add or update cart model."""
    request_data = json.loads(request.body.decode("utf-8"))

    product_slug = request_data["product_slug"]
    product_parameter_value = request_data["product_parameter_value"]
    user = request.user

    product_parameter_value = ProductParameterValue.objects.get(
        value=product_parameter_value, product__slug=product_slug
    )
    cart, _ = Cart.objects.get_or_create(user=user)

    ammount_product, is_new_ammount_product = CartAmmountProduct.objects.get_or_create(
        user=user, product_parameter=product_parameter_value
    )
    if is_new_ammount_product:
        ammount_product.ammount = 1
    else:
        ammount_product.ammount += 1
    ammount_product.save()

    cart.products.add(ammount_product)
    cart.save()

    return JsonResponse({"cart": cart.pk})
