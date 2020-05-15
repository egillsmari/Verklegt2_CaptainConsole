from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from myAccount.validation.validate import validateCVV, validateCardNumber
from django_countries.data import COUNTRIES
from myAccount.models import Zip



class locationForm(forms.Form):
    zip = forms.IntegerField()
    country = forms.ChoiceField(choices = sorted(COUNTRIES.items()))
    city = forms.CharField(max_length=255)
    class Meta:
        model = Zip
        fields = ('zip', 'country', 'city')


class SignUpForm(UserCreationForm):
    address = forms.CharField(max_length=255)
    addressNumber = forms.CharField(max_length=255)
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2', 'address', 'addressNumber', 'image')

widget=forms.TextInput(attrs={'placeholder': '16 of length ex. 1234123412341234'})

class PaymentForm(forms.Form):
    nameOnCard = forms.CharField(max_length=255)
    cardNumber = forms.CharField(validators=[validateCardNumber], widget=forms.TextInput(attrs={'placeholder': '16 of length ex. 1234123412341234'}))
    expirationDate = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'month first and then year with no space ex. 0222'}))
    CVV = forms.IntegerField(validators=[validateCVV], widget=forms.TextInput(attrs={'placeholder': '3 of length ex. 123'}))
    class Meta:
        model = User
        fields = ('nameOnCard', 'cardNumber', 'expirationDate', 'CVV')

class AccountUpdate(UserChangeForm):
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image')

class PaymentUpdate(UserChangeForm):
    pass


class ShippingUpdate(UserChangeForm):
    address = forms.CharField(max_length=255)
    addressNumber = forms.CharField(max_length=255)

    class Meta:
        model = User
        exclude = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image']
        fields = ('address', 'addressNumber')


