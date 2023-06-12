# Generated by Django 4.2.1 on 2023-06-12 09:21

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0013_alter_product_linked_parameter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]