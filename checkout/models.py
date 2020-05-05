from django.db import models
from myAccount.models import Account
from product.models import Product

# Create your models here.

class Order(models.Model):
    accountId = models.ForeignKey(Account, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

class Sold(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)