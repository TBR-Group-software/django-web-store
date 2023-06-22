from django.db import models
from .product.product_parameter_value_model import ProductParameterValue
from django.contrib.auth.models import User


class CartAmmountProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_parameter = models.ForeignKey(
        ProductParameterValue, null=False, blank=False, on_delete=models.CASCADE
    )
    ammount = models.PositiveIntegerField(blank=False, null=False, default=1)

    def __str__(self) -> str:
        return (
            f"{self.user.username} {self.product_parameter.product.name} {self.ammount}"
        )

    class Meta:
        """Meta for unique_together."""

        unique_together = ["user", "product_parameter"]
