from django.contrib import admin
from django.utils.html import format_html

from image_cropping import ImageCroppingMixin

from user_interface.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_type", "image_tag", "content_type")
    list_filter = ("image_type", "content_type")
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px; float:right;"/>'
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True
