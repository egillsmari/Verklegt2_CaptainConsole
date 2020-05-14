from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myAccount.models import Account, PaymentInfo
from myAccount.forms.forms import SignUpForm, PaymentForm, locationForm, AccountUpdate, ShippingUpdate
from checkout.models import Order, Sold
from myAccount.models import Zip
from context.contextBuilder import manufacturerContext
from django.contrib.auth.models import User

username = ''
password = ''

from myAccount.models import SearchHistory
from product.models import Product

def locationRegister(request):
    context = manufacturerContext(request)
    formLocation = locationForm(data=request.POST)
    if request.method == 'POST':
        if formLocation.is_valid():
            userZip = formLocation.cleaned_data.get('zip')
            userCountry = formLocation.cleaned_data.get('country')
            userCity = formLocation.cleaned_data.get('city')
            Zip.objects.create(zip=userZip, country=userCountry, city=userCity)
            if request.user.is_authenticated:
                return redirect('myAccount-updateAddress')
            else:
                return redirect('myAccount-register')
    else:
        formLocation = locationForm()
    context['form'] = formLocation
    return render(request, 'myAccount/locationInfo.html',  context)


def register(request):
    context = manufacturerContext(request)
    form = SignUpForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            account = user.account
            address = form.cleaned_data.get('address')
            addressNumber = form.cleaned_data.get('addressNumber')
            accountImage = form.cleaned_data.get('image')
            accountZip = Zip.objects.earliest('id')
            account.zip = accountZip
            account.addressNumber = addressNumber
            account.address = address
            account.accountImage = accountImage
            account.save()
            global username
            username = form.cleaned_data.get('username')
            global password
            password = form.cleaned_data.get('password1')
            return redirect('myAccount-paymentRegister')
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'myAccount/register.html', context)

def paymentRegister(request, src = 0):
    try:
        context = manufacturerContext(request)
        form = PaymentForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                nameOnCard = form.cleaned_data.get('nameOnCard')
                cardNumber = form.cleaned_data.get('cardNumber')
                expirationDate = form.cleaned_data.get('expirationDate')
                CVV = form.cleaned_data.get('CVV')
                if request.user.is_authenticated:
                    currentUser = request.user.id
                    savePayment = PaymentInfo(currentUser, nameOnCard, cardNumber, expirationDate, CVV)
                    savePayment.save()
                    if src == 1:
                        return redirect('checkout-payment')
                    elif src == 2:
                        return redirect('myAccount-paymentInfo')
                else:
                    currentUser = Account.objects.latest('id')
                    savePayment = PaymentInfo(currentUser.id, nameOnCard, cardNumber, expirationDate, CVV)
                    savePayment.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                return redirect('homepage-index')
        else:
            form = PaymentForm()
        context['form'] = form
        return render(request, 'myAccount/paymentRegister.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))

@login_required
def seePurchasehistory(request):
    context = manufacturerContext(request)
    context['products'] = []
    userId = request.user.id
    for order in Order.objects.all():
        if order.accountId_id == userId:
            for sold in Sold.objects.all():
                if sold.orderId_id == order.id:
                    context['products'].append(sold)
    return render(request, 'myAccount/pruchaseHistory.html', context)

@login_required
def accountInfo(request):
    return render(request, 'myAccount/accountInfo.html')

@login_required
def searchHistory(request):
    searchList = []
    context = manufacturerContext(request)
    userId = request.user.id
    searches = SearchHistory.objects.filter(accountId_id=userId).values_list('searchedItem', flat=True)
    for search in searches:
        searchList.append({search: Product.objects.filter(name__icontains=search)})
    context['searched'] = searchList
    return render(request, 'myAccount/searchHistory.html', context)

def paymentInfo(request):
    context = manufacturerContext(request)
    context['users'] = User.objects.all()
    userId = request.user.id
    context['payment'] = PaymentInfo.objects.filter(accountId_id=userId)
    return render(request, 'myAccount/paymentInfo.html', context)

def getAddress(request):
    for account in Account.objects.all():
        if account.user_id == request.user.id:
            return account.address

def updateAccount(request):
    context = manufacturerContext(request)
    if request.method == 'POST':
        form = AccountUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            account = user.account
            account.accountImage = form.cleaned_data.get('image')
            account.save()
            return render(request, 'myAccount/accountInfo.html', context)
    else:
        form = AccountUpdate(instance=request.user)
        context['form'] = form
        return render(request, 'myAccount/updateAccount.html', context)


def updateAddress(request):
    context = manufacturerContext(request)
    if request.method == 'POST':
        form = ShippingUpdate(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            account = user.account
            address = form.cleaned_data.get('address')
            addressNumber = form.cleaned_data.get('addressNumber')
            accountZip = Zip.objects.earliest('id')
            account.zip = accountZip
            account.addressNumber = addressNumber
            account.address = address
            account.save()
            return redirect('checkout-payment')
    else:
        form = ShippingUpdate(instance=request.user)
    context['form'] = form
    return render(request, 'myAccount/updateAddress.html', context)
