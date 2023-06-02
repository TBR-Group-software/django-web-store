from django.contrib import admin

from user_interface.models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    search_fields = ("category",)
