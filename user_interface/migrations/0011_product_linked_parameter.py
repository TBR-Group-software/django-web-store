# Generated by Django 4.2.1 on 2023-06-09 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0010_productattribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='linked_parameter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_interface.productparameter'),
            preserve_default=False,
        ),
    ]
