from django.forms import ModelForm, widgets
from django.shortcuts import render, redirect
from myAccount.models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['id', 'user']
        widgets = {'profile_image': widgets.TimeInput(attrs={'class':'form-control'}),

                   }