from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from user_interface.models import Cart


class CarttView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cart = Cart.objects.get(user=request.user)
        print(cart.products.all())
        return render(request, "cart.html", {"cart": cart})
