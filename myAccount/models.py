from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Zip(models.Model):
    zip = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)

class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, default=101)
    address = models.CharField(max_length=255, null=True, blank=True)
    addressNumber = models.CharField(max_length=20, null=True, blank=True)
    accountImage = models.ImageField(blank=True, null=True, upload_to='images/')


class PaymentInfo(models.Model):
    accountId = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='payment', on_delete=models.CASCADE)
    nameOnCard = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=255)
    expirationDate = models.CharField(max_length=25)
    CVV = models.IntegerField()


class SearchHistory(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='search', on_delete=models.CASCADE)
    searchedItem = models.CharField(max_length=255)


@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user = instance)
    instance.account.save()

