from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django_countries.data import COUNTRIES
from checkout.models import Order, Sold


class OrderForm(forms.Form):
    account = forms.IntegerField()
    product = forms.IntegerField()
    shippingMethod = forms.CharField(max_length=10)
    class Meta:
        model = Order
        fields = ('zip', 'country', 'city')


