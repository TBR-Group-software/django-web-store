# Generated by Django 4.2.1 on 2023-06-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0006_alter_product_slug_alter_productcategory_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
