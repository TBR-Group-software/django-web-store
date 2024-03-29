from django.contrib import admin

from product.models import ProductParameterValue


@admin.register(ProductParameterValue)
class ProductParameterValueAdmin(admin.ModelAdmin):
    list_display = ("product", "value", "product_parameter", "stock")
    list_filter = ("product_parameter", "value")
    search_fields = ("product_parameter", "value", "product")
