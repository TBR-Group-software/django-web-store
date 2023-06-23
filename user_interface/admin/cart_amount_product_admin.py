from django.contrib import admin

from user_interface.models import CartAmountProduct


@admin.register(CartAmountProduct)
class CartamountProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product_parameter", "amount")
    search_fields = ("user",)
