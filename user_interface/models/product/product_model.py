from django.db import models
from django.template.defaultfilters import slugify


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=255, unique=True)
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    linked_products = models.ManyToManyField("self", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
