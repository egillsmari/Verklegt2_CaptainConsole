# Generated by Django 2.2 on 2020-05-13 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_condition'),
        ('checkout', '0003_remove_order_productid'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='productId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]