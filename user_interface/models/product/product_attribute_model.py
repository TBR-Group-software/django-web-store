from django.db import models
from .product_parameter_model import ProductParameter


class ProductAttribute(models.Model):
    product_parameter = models.ForeignKey(ProductParameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_parameter} {self.value}"

    class Meta:
        """Meta for unique_together."""

        unique_together = ["product_parameter", "value"]
