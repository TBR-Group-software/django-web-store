from django.contrib import admin

from user_interface.models import Cart


@admin.register(Cart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user",)
    filter_horizontal = ("products",)
