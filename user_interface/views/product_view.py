from django.views import View
from user_interface.models import Product, ProductImage, ProductParameterValue
from django.shortcuts import render


class ProductView(View):
    def get(self, request, product_slug: str):
        product = Product.objects.get(slug=product_slug)
        parameter_values = ProductParameterValue.objects.filter(product=product)
        sizes = parameter_values.filter(
            product_parameter__parameter="size"
        ).values_list("value", flat=True)
        colors = parameter_values.filter(
            product_parameter__parameter="color"
        ).values_list("value", flat=True)
        images = ProductImage.objects.filter(product=product).values_list(
            "image", flat=True
        )
        context = {
            "product": product,
            "sizes": sizes,
            "colors": colors,
            "images": images,
        }
        return render(
            request,
            "product.html",
            context=context,
        )
