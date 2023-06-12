# Generated by Django 4.2.1 on 2023-06-12 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0012_alter_product_linked_products_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='linked_parameter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_interface.productparameter'),
        ),
        migrations.AlterField(
            model_name='product',
            name='linked_products',
            field=models.ManyToManyField(blank=True, to='user_interface.product'),
        ),
    ]