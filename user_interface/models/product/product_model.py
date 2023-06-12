from django.db import models
from django.template.defaultfilters import slugify

from .product_category_model import ProductCategory
from .product_parameter_model import ProductParameter


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    linked_parameter = models.ForeignKey(
        ProductParameter, on_delete=models.CASCADE, blank=True, null=True
    )
    linked_products = models.ManyToManyField("self", blank=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
