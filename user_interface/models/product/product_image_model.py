from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from image_cropping import ImageRatioField


IMAGE_TYPES = (("MAIN", "Main"), ("ADDITIONAL", "Additional"))


class ProductImage(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ("product", "productcategory")},
    )
    image = models.ImageField(upload_to="product_images")
    cropping = ImageRatioField("image", "400x400")
    image_type = models.CharField(
        max_length=20, choices=IMAGE_TYPES, blank=False, null=False
    )

    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.image.name
