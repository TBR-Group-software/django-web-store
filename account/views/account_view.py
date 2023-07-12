from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class AccountView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            "account.html",
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        return render(request, "account:account")
