from django.views import View
from user_interface.models import Product
from django.shortcuts import render


class ProductView(View):
    def get(self, request, product_slug: str):
        product = Product.objects.get(slug=product_slug)
        return render(request, "product.html", context={"product": product})
