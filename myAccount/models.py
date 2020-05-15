from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from myAccount.validation.validate import validateCVV, validateCardNumber


''' model class for Zip table '''
class Zip(models.Model):
    zip = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)


''' model class for Account table, linked to Zip table with foreign key '''
class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, default=101)
    address = models.CharField(max_length=255, null=True, blank=True)
    addressNumber = models.CharField(max_length=20, null=True, blank=True)
    accountImage = models.ImageField(blank=True, null=True, upload_to='images/')


''' model class for PaymentInfo table '''
class PaymentInfo(models.Model):
    accountId = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='payment', on_delete=models.CASCADE)
    nameOnCard = models.CharField(max_length=255)
    cardNumber = models.CharField(validateCardNumber, max_length=16)
    expirationDate = models.CharField(max_length=25)
    CVV = models.IntegerField(validateCVV)


''' model class for SearchHistory table, linked to Account table with foreign key '''
class SearchHistory(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='search', on_delete=models.CASCADE)
    searchedItem = models.CharField(max_length=255)


''' function activates when a user is created, creates an account for created user '''
@receiver(post_save, sender = User)
def create_user_profile( sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()

