# Generated by Django 2.1 on 2020-05-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]
