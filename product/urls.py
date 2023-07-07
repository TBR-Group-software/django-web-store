from django.urls import path

from .views import ProductView

urlpatterns = [
    path("<slug:product_slug>", ProductView.as_view(), name="product"),
]
