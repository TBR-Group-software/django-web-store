from django.contrib import admin

from user_interface.models import ProductParameter


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ("product", "parameter")
    list_filter = ("product", "parameter")
    search_fields = ("product", "parameter")
