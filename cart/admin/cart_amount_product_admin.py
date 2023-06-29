from django.contrib import admin

from cart.models import CartAmountProduct


@admin.register(CartAmountProduct)
class CartamountProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product_parameter", "amount")
    search_fields = ("user",)
