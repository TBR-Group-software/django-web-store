from django.db import models
from django.contrib.auth.models import User

from product.models import ProductParameterValue


class CartAmountProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_parameter = models.ForeignKey(
        ProductParameterValue, null=False, blank=False, on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(blank=False, null=False, default=1)

    def __str__(self) -> str:
        return (
            f"{self.user.username} {self.product_parameter.product.name} {self.amount}"
        )

    class Meta:
        """Meta for unique_together."""

        unique_together = ["user", "product_parameter"]
        ordering = ["product_parameter__product__name"]
