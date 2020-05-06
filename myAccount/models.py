from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Zip(models.Model):
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class PaymentInfo(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nameOnCard = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=255)
    CVV = models.FloatField()


class SearchHistory(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    searchedItem = models.CharField(max_length=255)

