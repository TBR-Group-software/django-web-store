from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from review.models import Review
from product.models import Product


class ReviewsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        reviews = Review.objects.all()
        return render(
            request,
            "reviews.html",
            {"reviews": reviews, "page_title": "Reviews"},
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user

        review_stars = int(request.POST["star-input"][0])
        review_text = request.POST["text"]
        review_product = Product.objects.get(id=request.POST["product_id"][0])

        Review.objects.create(
            user=user,
            product=review_product,
            stars=review_stars,
            text=review_text,
        )

        return redirect(
            reverse("product:product", kwargs={"product_slug": review_product.slug})
        )
