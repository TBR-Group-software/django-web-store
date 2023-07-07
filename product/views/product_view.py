from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from product.models import Product, ProductImage, ProductParameterValue
from review.models import Review


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
        reviews = Review.objects.filter(product=product)
        context = {
            "product": product,
            "sizes": sizes,
            "images": images,
            "reviews": reviews,
        }

        return render(
            request,
            "product.html",
            context=context,
        )
