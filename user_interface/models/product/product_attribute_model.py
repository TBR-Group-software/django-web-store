from django.db import models
from .product_parameter_model import ProductParameter
from .product_model import Product


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_parameter = models.ForeignKey(ProductParameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.product.name

    class Meta:
        """Meta for unique_together."""

        unique_together = ["product", "product_parameter", "value"]