from django.contrib import admin

from product.models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    search_fields = ("category",)
