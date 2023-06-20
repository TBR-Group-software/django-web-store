from django.db import models
from django.contrib.auth.models import User

from .product.product_parameter_value_model import ProductParameterValue


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    products = models.ManyToManyField(ProductParameterValue)

    def __str__(self) -> str:
        return self.user.username
