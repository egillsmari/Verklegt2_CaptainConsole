# Generated by Django 3.0.6 on 2020-05-08 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200508_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='manufacturer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.Manufacturer'),
        ),
    ]
