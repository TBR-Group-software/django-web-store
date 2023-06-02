from django.contrib import admin

from user_interface.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "created_at")
    search_fields = ("name", "price", "description")
