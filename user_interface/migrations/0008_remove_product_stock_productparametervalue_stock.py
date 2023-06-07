# Generated by Django 4.2.1 on 2023-06-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0007_product_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='productparametervalue',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]