# Generated by Django 2.2 on 2020-05-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAccount', '0015_auto_20200511_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
