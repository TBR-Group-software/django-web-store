from django.contrib import admin

from product.models import ProductParameter


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ("parameter",)
    search_fields = ("parameter",)
