# Generated by Django 4.2.1 on 2023-06-06 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0004_product_linked_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productparameter',
            name='product',
        ),
        migrations.AddField(
            model_name='productparametervalue',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_interface.product'),
            preserve_default=False,
        ),
    ]
