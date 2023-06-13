from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from user_interface.models import (
    ProductCategory,
    Product,
    ProductParameterValue,
    ProductAttribute,
)


class ProductCategoryView(View):
    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        filters = dict(request.GET)
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, active=True)

        context = self._get_product_context(category, products, filters)
        if len(filters) > 0:
            filtred_products = self.filter_products(products, filters)
        else:
            filtred_products = products
        context["products"] = filtred_products

        return render(request, "category.html", context=context)

    def _get_product_context(
        self,
        category: ProductCategory,
        products: QuerySet[Product],
        active_filters: dict,
    ) -> dict:
        parameter_value_filter = self._get_parameter_values(products)
        product_attributes = self._get_product_attributes(products)

        parameter_value_filter.update(product_attributes)

        filters = self._set_filters_checked(active_filters, parameter_value_filter)

        return {"category": category, "filters": filters}

    def _get_parameter_values(self, products: QuerySet[Product]) -> dict:
        product_parameter_values = ProductParameterValue.objects.filter(
            product__in=products, stock__gte=1
        )
        product_parameters = product_parameter_values.distinct(
            "product_parameter__parameter"
        ).values_list("product_parameter__parameter", flat=True)
        return {
            parameter: [
                {"checked": False, "value": value}
                for value in product_parameter_values.filter(
                    product_parameter__parameter=parameter
                )
                .distinct("value")
                .order_by("value")
                .values_list("value", flat=True)
            ]
            for parameter in product_parameters
        }

    def _get_product_attributes(self, products: QuerySet[Product]) -> dict:
        product_attributes = (
            ProductAttribute.objects.filter(product__in=products)
            .distinct("product_parameter__parameter")
            .values_list("product_parameter__parameter", flat=True)
        )
        return {
            parameter: [
                {"checked": False, "value": value}
                for value in product_attributes.filter(
                    product_parameter__parameter=parameter
                )
                .distinct("value")
                .order_by("value")
                .values_list("value", flat=True)
            ]
            for parameter in product_attributes
        }

    def _set_filters_checked(self, active_filters: dict, all_filters: dict) -> dict:
        for filter_key, active_filter_value in active_filters.items():
            if active_filter_value:
                for all_filter_value in all_filters[filter_key]:
                    if all_filter_value["value"] in active_filter_value:
                        all_filter_value["checked"] = True

        return all_filters

    def filter_products(
        self, products: QuerySet[Product], filters: dict
    ) -> QuerySet[Product]:
        filtred_product_ids = []
        parameter_product_filtred = ProductParameterValue.objects.filter(
            product__in=products
        )
        product_attribute_filtered = ProductAttribute.objects.filter(
            product__in=products
        )
        for filter_key in filters.keys():
            filterd_parameters = parameter_product_filtred.filter(
                product_parameter__parameter=filter_key, value__in=filters[filter_key]
            ).values_list("product__id", flat=True)
            if filterd_parameters:
                filtred_product_ids.append(filterd_parameters)

            filtred_attributes = product_attribute_filtered.filter(
                product_parameter__parameter=filter_key, value__in=filters[filter_key]
            ).values_list("product__id", flat=True)
            if filtred_attributes:
                filtred_product_ids.append(filtred_attributes)

        filtered_product = set(filtred_product_ids[0])

        for sublist in filtred_product_ids[1:]:
            filtered_product = filtered_product.intersection(sublist)

        return products.filter(id__in=filtered_product)
