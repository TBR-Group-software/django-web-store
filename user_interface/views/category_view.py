from enum import Enum

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
    DEFAULT_PARAMETERS = ["minPrice", "maxPrice", "stock", "sort"]
    DEFAULT_SORT = "-in_stock"

    class SortType(Enum):
        """Category sort types."""

        OLDER = "older"
        NEWER = "newer"
        CHEAPER = "cheaper"
        EXPENSIVE = "expensive"

    def get(self, request: HttpRequest, category_slug: str) -> HttpResponse:
        query_parameters = dict(request.GET)
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)

        if query_parameters.get("sort"):
            products = self._sort_products(products, query_parameters["sort"][0])

        context = self._get_product_context(category, products, query_parameters)
        if len(query_parameters) > 0:
            filtred_products = self.filter_products(products, query_parameters)
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

        min_price, max_price = self._get_price_filter_values(active_filters)
        in_stock, out_of_stock = self._get_stock_values(active_filters)

        return {
            "category_name": category.category,
            "page_title": category.category,
            "filters": filters,
            "min_price": min_price,
            "max_price": max_price,
            "in_stock": in_stock,
            "out_of_stock": out_of_stock,
            "sort_types": [type.value for type in self.SortType],
        }

    def _get_price_filter_values(self, filters: dict) -> tuple:
        min_price = None
        max_price = None

        if filters.get("minPrice"):
            min_price = int(filters["minPrice"][0])

        if filters.get("maxPrice"):
            max_price = int(filters["maxPrice"][0])

        return min_price, max_price

    def _get_stock_values(self, filters: dict) -> tuple:
        in_stock = False
        out_of_stock = False

        if filters.get("stock"):
            if "in-stock" in filters["stock"]:
                in_stock = True
            if "out-of-stock" in filters["stock"]:
                out_of_stock = True

        return in_stock, out_of_stock

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
            if filter_key in self.DEFAULT_PARAMETERS:
                continue
            if active_filter_value:
                for all_filter_value in all_filters[filter_key]:
                    if all_filter_value["value"] in active_filter_value:
                        all_filter_value["checked"] = True

        return all_filters

    def _sort_products(
        self, products: QuerySet[Product], sort_type: str
    ) -> QuerySet[Product]:
        match sort_type:
            case self.SortType.OLDER.value:
                products = products.order_by(self.DEFAULT_SORT, "created_at")
            case self.SortType.NEWER.value:
                products = products.order_by(self.DEFAULT_SORT, "-created_at")
            case self.SortType.CHEAPER.value:
                products = products.order_by(self.DEFAULT_SORT, "price")
            case self.SortType.EXPENSIVE.value:
                products = products.order_by(self.DEFAULT_SORT, "-price")
            case _:
                pass

        return products

    def filter_products(
        self, products: QuerySet[Product], filters: dict
    ) -> QuerySet[Product]:
        parameter_product_filtred = ProductParameterValue.objects.filter(
            product__in=products
        )
        product_attribute_filtered = ProductAttribute.objects.filter(
            product__in=products
        )
        for filter_key in filters.keys():
            if filter_key == "sort":
                continue
            filtred_product_ids = []
            if filter_key == "minPrice" or filter_key == "maxPrice":
                value = int(filters[filter_key][0])
                if filter_key == "minPrice":
                    filtred_product_ids.append(
                        products.filter(price__gte=value).values_list("id", flat=True)
                    )
                else:
                    filtred_product_ids.append(
                        products.filter(price__lte=value).values_list("id", flat=True)
                    )
            elif filter_key == "stock":
                values = filters[filter_key]
                if len(values) >= 2:
                    continue
                value = True if filters[filter_key][0] == "in-stock" else False
                filtred_product_ids.append(
                    products.filter(in_stock=value).values_list("id", flat=True)
                )
            else:
                filterd_parameters = parameter_product_filtred.filter(
                    product_parameter__parameter=filter_key,
                    value__in=filters[filter_key],
                ).values_list("product__id", flat=True)
                if filterd_parameters:
                    filtred_product_ids.append(filterd_parameters)

                filtred_attributes = product_attribute_filtered.filter(
                    product_parameter__parameter=filter_key,
                    value__in=filters[filter_key],
                ).values_list("product__id", flat=True)
                if filtred_attributes:
                    filtred_product_ids.append(filtred_attributes)

            if len(filtred_product_ids) > 0:
                products = products.filter(id__in=filtred_product_ids)

        return products
