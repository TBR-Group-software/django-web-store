from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from user_interface.models import Product, ProductImage, ProductParameterValue


class ProductView(View):
    def get(self, request: HttpRequest, product_slug: str) -> HttpResponse:
        product = Product.objects.get(slug=product_slug)
        sizes = (
            ProductParameterValue.objects.filter(
                product=product, product_parameter__parameter="Size"
            )
            .order_by("value")
            .values("value", "stock")
        )

        images = ProductImage.objects.filter(
            object_id=product.pk, content_type__model="product"
        )
        context = {
            "product": product,
            "sizes": sizes,
            "images": images,
        }

        return render(
            request,
            "product.html",
            context=context,
        )
