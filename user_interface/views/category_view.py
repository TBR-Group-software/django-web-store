from django.http import HttpRequest, HttpResponse
from django.views import View
from user_interface.models import (
    ProductCategory,
    Product,
    ProductParameterValue,
    ProductAttribute,
)
from django.shortcuts import render


class ProductCategoryView(View):
    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, active=True)

        product_parameter_values = ProductParameterValue.objects.filter(
            product__in=products, stock__gte=1
        )
        product_parameters = product_parameter_values.distinct(
            "product_parameter__parameter"
        ).values_list("product_parameter__parameter", flat=True)
        parameter_value_filter = [
            {
                parameter: list(
                    product_parameter_values.filter(
                        product_parameter__parameter=parameter
                    )
                    .distinct("value")
                    .order_by("value")
                    .values_list("value", flat=True)
                )
            }
            for parameter in product_parameters
        ]

        product_attributes = (
            ProductAttribute.objects.filter(product__in=products)
            .distinct("product_parameter__parameter")
            .values_list("product_parameter__parameter", flat=True)
        )
        attribute_filters = [
            {
                parameter: list(
                    product_attributes.filter(product_parameter__parameter=parameter)
                    .distinct("value")
                    .order_by("value")
                    .values_list("value", flat=True)
                )
            }
            for parameter in product_attributes
        ]

        print(parameter_value_filter)
        print(attribute_filters)

        return render(
            request,
            "category.html",
            context={
                "category": category,
                "products": products,
                "parameter_value_filter": parameter_value_filter,
                "attribute_filters": attribute_filters,
            },
        )
