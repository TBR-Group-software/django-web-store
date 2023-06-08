from django.http import HttpRequest, HttpResponse
from django.views import View
from user_interface.models import ProductCategory, Product
from django.shortcuts import render


class ProductCategoryView(View):
    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, active=True)

        return render(
            request,
            "category.html",
            context={"category": category, "products": products},
        )
