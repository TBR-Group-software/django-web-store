from django.urls import path

from .views import IndexView, ProductView, ProductCategoryView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<slug:product_slug>", ProductView.as_view(), name="product"),
    path(
        "category/<slug:category_slug>", ProductCategoryView.as_view(), name="category"
    ),
]
