# Generated by Django 4.2.1 on 2023-06-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0009_remove_productcategory_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.product')),
                ('product_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interface.productparameter')),
            ],
            options={
                'unique_together': {('product', 'product_parameter', 'value')},
            },
        ),
    ]
