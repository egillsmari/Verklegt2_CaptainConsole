# Generated by Django 2.2 on 2020-05-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_sold_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sold',
            name='productId',
        ),
        migrations.AddField(
            model_name='sold',
            name='image',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='sold',
            name='name',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='sold',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
