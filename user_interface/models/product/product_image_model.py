from django.db import models
from .product_model import Product


IMAGE_TYPES = (("MAIN", "Main"), ("ADDITIONAL", "Additional"))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")
    image_type = models.CharField(
        max_length=20, choices=IMAGE_TYPES, blank=False, null=False
    )

    def __str__(self):
        return self.product.name
