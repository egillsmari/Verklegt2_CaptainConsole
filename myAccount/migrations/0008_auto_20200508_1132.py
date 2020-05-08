# Generated by Django 2.1 on 2020-05-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAccount', '0007_remove_account_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountImage',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='addressNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
