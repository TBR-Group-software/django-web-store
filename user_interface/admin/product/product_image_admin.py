from django.contrib import admin

from user_interface.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "image_type")
    search_fields = ("product", "image")
    list_filter = ("image_type",)
