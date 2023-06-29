import json
from django.http import HttpRequest, JsonResponse

from cart.models import Cart, CartAmountProduct
from product.models import ProductParameterValue


def edit_cart_view(request: HttpRequest) -> JsonResponse:
    """Add or update cart model."""
    request_data = json.loads(request.body.decode("utf-8"))
    operation_type = request_data.get("operation_type")

    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user)

    if operation_type == "add_product":
        product_slug = request_data.get("product_slug")
        product_parameter_value = request_data.get("product_parameter_value")

        try:
            product_parameter_value = ProductParameterValue.objects.get(
                value=product_parameter_value, product__slug=product_slug
            )
        except ProductParameterValue.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid product parameter value or slug"}, status=500
            )

        amount_product, _ = CartAmountProduct.objects.get_or_create(
            user=user, product_parameter=product_parameter_value
        )
        amount_product.amount = 1
        amount_product.save()
        cart.products.add(amount_product)

    elif operation_type == "cart_plus":
        cart_amount_product_id = request_data.get("cart_amount_id")
        try:
            cart_amount_product = CartAmountProduct.objects.get(
                id=cart_amount_product_id
            )
        except CartAmountProduct.DoesNotExist:
            return JsonResponse({"error": "Invalid cart amount product ID"}, status=500)

        if (
            cart_amount_product.amount + 1
            <= cart_amount_product.product_parameter.stock
        ):
            cart_amount_product.amount += 1
            cart_amount_product.save()
        else:
            return JsonResponse({"error": "Max product added"}, status=500)

    elif operation_type == "cart_minus":
        cart_amount_product_id = request_data.get("cart_amount_id")
        try:
            cart_amount_product = CartAmountProduct.objects.get(
                id=cart_amount_product_id
            )
        except CartAmountProduct.DoesNotExist:
            return JsonResponse({"error": "Invalid cart amount product ID"}, status=500)

        if cart_amount_product.amount - 1 > 0:
            cart_amount_product.amount -= 1
            cart_amount_product.save()
        else:
            return JsonResponse(
                {"error": "You cannot have a negative product amount"}, status=500
            )

    elif operation_type == "cart_remove":
        cart_amount_product_id = request_data.get("cart_amount_id")
        try:
            cart_amount_product = CartAmountProduct.objects.get(
                id=cart_amount_product_id
            )
        except CartAmountProduct.DoesNotExist:
            return JsonResponse({"error": "Invalid cart amount product ID"}, status=500)

        cart_amount_product.delete()

    else:
        return JsonResponse(
            {"error": f"Unknown operation {operation_type}"}, status=500
        )

    cart.save()
    return JsonResponse({"cart": cart.pk})
