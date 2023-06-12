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
        filters = dict(request.GET)
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, active=True)

        context = self._get_product_context(category=category, products=products)

        if len(filters) > 0:
            filtred_products = self.filter_products(products, filters)
        else:
            filtred_products = products
        context.update({"products": filtred_products})

        return render(request, "category.html", context=context)

    def _get_product_context(self, category, products) -> dict:
        parameter_value_filter = self._get_parameter_values(products=products)
        product_attributes = self._get_product_atrributes(products=products)

        parameter_value_filter.extend(product_attributes)

        return {
            "category": category,
            "filters": parameter_value_filter,
        }

    def _get_parameter_values(self, products) -> list:
        product_parameter_values = ProductParameterValue.objects.filter(
            product__in=products, stock__gte=1
        )
        product_parameters = product_parameter_values.distinct(
            "product_parameter__parameter"
        ).values_list("product_parameter__parameter", flat=True)
        return [
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

    def _get_product_atrributes(self, products) -> list:
        product_attributes = (
            ProductAttribute.objects.filter(product__in=products)
            .distinct("product_parameter__parameter")
            .values_list("product_parameter__parameter", flat=True)
        )
        return [
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

    def filter_products(self, products, filters):
        filtred_product_parameters_ids = []
        filtred_product_attribute_ids = []
        parameter_product_filtred = ProductParameterValue.objects.filter(
            product__in=products
        )
        product_attribute_filterd = ProductAttribute.objects.filter(
            product__in=products
        )
        for filter_key in filters.keys():
            filtred_product_parameters_ids.extend(
                parameter_product_filtred.filter(
                    product_parameter__parameter=filter_key,
                    value__in=filters[filter_key],
                ).values_list("product__id", flat=True)
            )
            filtred_product_attribute_ids.extend(
                product_attribute_filterd.filter(
                    product_parameter__parameter=filter_key,
                    value__in=filters[filter_key],
                ).values_list("product__id", flat=True)
            )

        return products.filter(
            id__in=set(filtred_product_parameters_ids)
            & set(filtred_product_attribute_ids)
        )
