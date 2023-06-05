from django.views import View
from user_interface.models import ProductCategory
from django.shortcuts import render


class ProductCategoryView(View):
    def get(self, request, category_slug: str):
        category = ProductCategory.objects.get(slug=category_slug)

        return render(request, "category.html", context={"category": category})
