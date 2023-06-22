from django.db import models
from django.contrib.auth.models import User

from .cart_ammount_product_model import CartAmmountProduct


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    products = models.ManyToManyField(CartAmmountProduct)

    def __str__(self) -> str:
        return self.user.username
