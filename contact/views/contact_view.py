from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from contact.models.question_model import Question
from django.contrib import messages


class ContactView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "contact.html", context={"page_title": "Contact us"})

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        text = request.POST["text"]

        Question.objects.create(user=user, text=text)
        messages.success(
            request, "You have been sent a question, wait for a reply in your email."
        )

        return render(request, "contact.html")
