# Generated by Django 2.2 on 2020-05-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shippingMethod',
            field=models.CharField(default='pickUp', max_length=10),
        ),
    ]