from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from product.models import ProductImage


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = self.__get_products()
        context = {
            "page_title": "Shoes store",
            "main_products": self.get_main_products(products),
            "popular_products": self.get_post_popular_products(products),
        }
        return render(request, "index.html", context=context)

    def get_main_products(self, products: QuerySet[ProductImage]):
        # TODO make relevance logic

        return products[:3]

    def get_post_popular_products(self, products: QuerySet[ProductImage]):
        # TODO make popular logic

        return products[3:13]

    def __get_products(self):
        return ProductImage.objects.filter(
            content_type__model="product", image_type="MAIN"
        )
