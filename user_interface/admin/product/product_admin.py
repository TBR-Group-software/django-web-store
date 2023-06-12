from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models.fields.related import ManyToManyField

from user_interface.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "short_description",
        "created_at",
        "category",
        "linked_parameter",
        "active",
    )
    search_fields = ("name", "price", "short_description")
    filter_horizontal = ("linked_products", "product_attributes")
    list_filter = ("category", "linked_parameter")
    list_editable = ("active",)

    def formfield_for_manytomany(
        self, db_field: ManyToManyField, request: HttpRequest, **kwargs
    ):
        if db_field.name == "linked_products":
            obj_id = (
                request.resolver_match.kwargs.get("object_id")
                if request.resolver_match.kwargs
                else None
            )
            if obj_id:
                kwargs.update({"queryset": Product.objects.exclude(id=obj_id)})
        return super().formfield_for_manytomany(db_field, request, **kwargs)
