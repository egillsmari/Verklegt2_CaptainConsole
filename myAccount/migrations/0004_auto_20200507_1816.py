# Generated by Django 2.1 on 2020-05-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAccount', '0003_auto_20200506_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='cardNumber',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='nameOnCard',
            field=models.CharField(max_length=255),
        ),
    ]
