# Generated by Django 2.2 on 2020-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default='unknown', max_length=50),
            preserve_default=False,
        ),
    ]
