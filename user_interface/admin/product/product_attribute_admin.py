from django.contrib import admin

from user_interface.models import ProductAttribute


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("product_parameter", "value", "product")
    list_filter = ("product_parameter", "value")
    search_fields = ("product_parameter", "value", "product")
