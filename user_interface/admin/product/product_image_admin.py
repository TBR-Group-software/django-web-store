from django.contrib import admin

from image_cropping import ImageCroppingMixin

from user_interface.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("product", "image", "image_type")
    search_fields = ("product", "image")
    list_filter = ("image_type",)
