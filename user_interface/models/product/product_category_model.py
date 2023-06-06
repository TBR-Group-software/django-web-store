from django.db import models
from .product_model import Product
from django.template.defaultfilters import slugify


class ProductCategory(models.Model):
    product = models.ManyToManyField(Product)
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(ProductCategory, self).save(*args, **kwargs)
