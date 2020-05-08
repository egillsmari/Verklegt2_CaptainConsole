from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Zip(models.Model):
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, default=101)
    address = models.CharField(max_length=10, null=True, blank=True)
    addressNumber = models.CharField(max_length=20, null=True, blank=True)
    accountImage = models.CharField(max_length=999, null=True, blank=True)


class PaymentInfo(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nameOnCard = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=255)
    expirationDate = models.CharField(max_length=25)
    CVV = models.FloatField()


class SearchHistory(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    searchedItem = models.CharField(max_length=255)


@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user = instance)
    instance.account.save()

