from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from cart.models import Cart


class CarttView(View):
    @method_decorator(login_required, name="dispatch")
    def get(self, request: HttpRequest) -> HttpResponse:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        total_price = self.calculate_total_price_of_cart(cart)
        return render(
            request,
            "cart.html",
            {"cart": cart, "total_price": total_price, "page_title": "Cart"},
        )

    def calculate_total_price_of_cart(self, cart: Cart) -> int:
        total_price = 0
        for item in cart.products.all():
            total_price += item.product_parameter.product.price * item.amount

        return int(total_price)
