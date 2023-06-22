from django.contrib import admin

from user_interface.models import CartAmmountProduct


@admin.register(CartAmmountProduct)
class CartAmmountProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product_parameter", "ammount")
    search_fields = ("user",)
