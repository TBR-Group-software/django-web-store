from django.db import models
from .product_model import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.product.name
