# Generated by Django 4.2.1 on 2023-06-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0003_productimage_image_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='linked_products',
            field=models.ManyToManyField(blank=True, to='user_interface.product'),
        ),
    ]
