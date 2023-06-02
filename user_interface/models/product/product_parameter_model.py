from django.db import models
from .product_model import Product


class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parameter = models.CharField(max_length=255)

    def __str__(self):
        return self.product.name
