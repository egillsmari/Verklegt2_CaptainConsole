# Generated by Django 3.0.5 on 2020-05-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('myAccount', '0001_initial'),
        ('checkout', '0002_auto_20200505_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAccount.Account')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
            ],
        ),
    ]
