from django.db import models
from .product_model import Product


class ProductCategory(models.Model):
    product = models.ManyToManyField(Product)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.product.name
