from django.contrib import admin

from user_interface.models import ProductParameterValue


@admin.register(ProductParameterValue)
class ProductParameterValueAdmin(admin.ModelAdmin):
    list_display = ("product_parameter", "value", "product", "stock")
    list_filter = ("product_parameter", "value")
    search_fields = ("product_parameter", "value", "product")
