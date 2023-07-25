from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include(("user_interface.urls", "user_interface"), namespace="user_interface"),
    ),
    path("product/", include(("product.urls", "product"), namespace="product")),
    path("category/", include(("category.urls", "category"), namespace="category")),
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),
    path("review/", include(("review.urls", "review"), namespace="review")),
    path("accounts/", include(("account.urls", "account"), namespace="account")),
    path("contact/", include(("contact.urls", "contact"), namespace="contact")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
