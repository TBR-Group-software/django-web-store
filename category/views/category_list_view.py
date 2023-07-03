from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from product.models import ProductCategory


class CategoryListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        categories = ProductCategory.objects.all()
        return render(
            request,
            "category_list.html",
            {"categories": categories, "page_title": "Categories"},
        )
