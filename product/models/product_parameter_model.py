from django.db import models


class ProductParameter(models.Model):
    parameter = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.parameter
