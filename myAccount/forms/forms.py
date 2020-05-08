from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myAccount.models import Zip


zipList = []
for zip in Zip.objects.all():
    zipList.append((zip.id, zip.id))


class SignUpForm(UserCreationForm):
    zipForm = forms.ChoiceField(choices=zipList)
    address = forms.CharField(max_length=255)
    addressNumber = forms.CharField(max_length=255)
    image = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2', 'address', 'addressNumber', 'image', 'zipForm' )