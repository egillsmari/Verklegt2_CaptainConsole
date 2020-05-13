from django.db import models
from django.conf import settings
from product.models import Product
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model):
    accountId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    shippingMethod = models.CharField(default='pickUp', max_length=10)

class Sold(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='unknown')
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=255, default='unknown')
