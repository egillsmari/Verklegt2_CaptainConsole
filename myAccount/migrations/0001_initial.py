# Generated by Django 3.0.5 on 2020-05-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('addressNum', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchedItem', models.CharField(max_length=255)),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAccount.Account')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOnCard', models.CharField(max_length=255)),
                ('cardNumber', models.CharField(max_length=255)),
                ('CVV', models.FloatField()),
                ('accountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAccount.Account')),
            ],
        ),
    ]
