from django.urls import path

from .views import ProductCategoryView, CategoryListView

urlpatterns = [
    path("<slug:category_slug>", ProductCategoryView.as_view(), name="category"),
    path("all/", CategoryListView.as_view(), name="category_list"),
]
