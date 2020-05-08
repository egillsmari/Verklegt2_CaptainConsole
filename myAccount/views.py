from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myAccount.forms.userForm import AccountForm
from myAccount.models import Account
from myAccount.forms.forms import SignUpForm
from myAccount.models import Zip


def register(request):
    form = SignUpForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            account = user.account
            address = form.cleaned_data.get('address')
            addressNumber = form.cleaned_data.get('addressNumber')
            accountImage = form.cleaned_data.get('accountImage')
            accountZipTemp = form.cleaned_data.get('zipForm')
            accountZip = Zip.objects.get(id=accountZipTemp)
            account.zip = accountZip
            account.addressNumber = addressNumber
            account.address = address
            account.accountImage = accountImage
            account.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage-index')
    return render(request, 'myAccount/register.html', {'form': form})

@login_required
def seePurchasehistory(request):
    return render(request, 'myAccount/pruchaseHistory.html')

@login_required
def accountInfo(request):
    account = Account.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AccountForm(instance=AccountForm, data=request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('homepage-index')
    return render(request, 'myAccount/accountInfo.html', {
        'form': AccountForm(instance=account)
    })
