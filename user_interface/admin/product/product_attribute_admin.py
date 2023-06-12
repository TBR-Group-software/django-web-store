from django.contrib import admin

from user_interface.models import ProductAttribute


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("value", "product_parameter")
    list_filter = ("product_parameter",)
    search_fields = ("product_parameter", "value")
