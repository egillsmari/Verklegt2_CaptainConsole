from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)
    dateOfBirth = models.DateTimeField()
    address = models.CharField(max_length=255)
    addressNum = models.CharField(max_length=255)
    password =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


class PaymentInfo(models.Model):
    accountId = models.ForeignKey(Account, models.CASCADE)
    nameOnCard = models.CharField(max_length=255)
    cardNumber = models.CharField(max_length=255)
    CVV = models.FloatField()


class SearchHistory(models.Model):
    accountId = models.ForeignKey(Account, on_delete=models.CASCADE)
    searchedItem = models.CharField(max_length=255)

class Zip(models.Model):
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
