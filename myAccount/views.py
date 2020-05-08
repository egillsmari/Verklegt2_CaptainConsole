from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myAccount.forms.userForm import AccountForm
from myAccount.models import Account
from myAccount.forms.forms import UserCreationForm



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'myAccount/register.html', {'form': UserCreationForm})

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
            account.username = request.user
            account.save()
            return redirect('homepage-index')
    return render(request, 'myAccount/accountInfo.html', {
        'form': AccountForm(instance=account)
    })
