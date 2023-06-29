from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation

from product.models import ProductImage


class ProductCategory(models.Model):
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    images = GenericRelation(ProductImage)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(ProductCategory, self).save(*args, **kwargs)
