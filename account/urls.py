from django.urls import path

from account.views import (
    user_login_view,
    user_logout_view,
    user_register_view,
    AccountView,
)

urlpatterns = [
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path("register/", user_register_view, name="register"),
    path("account/", AccountView.as_view(), name="account"),
]
