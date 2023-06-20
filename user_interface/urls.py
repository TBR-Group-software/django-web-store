from django.urls import path

from .views import (
    IndexView,
    ProductView,
    ProductCategoryView,
    CategoryListView,
    add_to_cart_view,
    CarttView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<slug:product_slug>", ProductView.as_view(), name="product"),
    path(
        "category/<slug:category_slug>", ProductCategoryView.as_view(), name="category"
    ),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("add_to_cart/", add_to_cart_view, name="add_to_cart"),
    path("cart", CarttView.as_view(), name="cart"),
]
