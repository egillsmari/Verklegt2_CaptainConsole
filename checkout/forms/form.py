from django import forms
from checkout.models import Order

'''Order form when user has completed his order'''
class OrderForm(forms.Form):
    account = forms.IntegerField()
    product = forms.IntegerField()
    shippingMethod = forms.CharField(max_length=10)
    class Meta:
        model = Order
        fields = ('zip', 'country', 'city')


