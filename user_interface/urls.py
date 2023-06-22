from django.urls import path

from .views import (
    IndexView,
    ProductView,
    ProductCategoryView,
    CategoryListView,
    edit_cart_view,
    CarttView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<slug:product_slug>", ProductView.as_view(), name="product"),
    path(
        "category/<slug:category_slug>", ProductCategoryView.as_view(), name="category"
    ),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("edit_cart/", edit_cart_view, name="edit_cart"),
    path("cart", CarttView.as_view(), name="cart"),
]
