from django.db import models
from django.contrib.auth.models import User

from .cart_amount_product_model import CartAmountProduct


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    products = models.ManyToManyField(CartAmountProduct)

    def __str__(self) -> str:
        return self.user.username
