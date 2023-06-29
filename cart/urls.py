from django.urls import path

from .views import (
    edit_cart_view,
    CarttView,
)

urlpatterns = [
    path("edit/", edit_cart_view, name="edit_cart"),
    path("", CarttView.as_view(), name="cart"),
]
