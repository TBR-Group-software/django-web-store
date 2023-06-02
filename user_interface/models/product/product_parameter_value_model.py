from django.db import models
from .product_parameter_model import ProductParameter


class ProductParameterValue(models.Model):
    product_parameter = models.ForeignKey(ProductParameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.product_parameter.product.name
