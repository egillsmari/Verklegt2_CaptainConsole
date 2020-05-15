from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from myAccount.models import Account, PaymentInfo
from myAccount.forms.forms import SignUpForm, PaymentForm, locationForm, AccountUpdate, ShippingUpdate
from checkout.models import Order, Sold
from myAccount.models import Zip
from context.contextBuilder import manufacturerContext
from django.contrib.auth.models import User
from myAccount.models import SearchHistory
from product.models import Product, ProductImage

username = ''
password = ''


''' handles location registration, gets form data via POST request, saves via models
 redirects to/renders appropriate page when finished'''
def locationRegister(request):
    context = manufacturerContext(request)

    # gets form data
    formLocation = locationForm(data=request.POST)

    # when the user has submitted the form
    if request.method == 'POST':
        if formLocation.is_valid():
            userZip = formLocation.cleaned_data.get('zip')
            userCountry = formLocation.cleaned_data.get('country')
            userCity = formLocation.cleaned_data.get('city')

            # saves data via Zip model
            Zip.objects.create(zip=userZip, country=userCountry, city=userCity)

            # if user is authenticated, redirects to update address, if not user is in sign up process
            if request.user.is_authenticated:
                return redirect('myAccount-updateAddress')
            else:
                return redirect('myAccount-register')

    # when function is initially called, empty form is sent via context
    else:
        formLocation = locationForm()
    context['form'] = formLocation
    return render(request, 'myAccount/locationInfo.html',  context)


''' handles user registration gets form data via POST request, saves data via models,
 redirects to/renders appropriate page when finished'''
def register(request):
    context = manufacturerContext(request)

    # gets form data and files
    form = SignUpForm(request.POST, request.FILES)

    # when the user has submitted the form
    if request.method == 'POST':
        if form.is_valid():

            # information saved into user table and account table
            user = form.save()
            account = user.account
            address = form.cleaned_data.get('address')
            addressNumber = form.cleaned_data.get('addressNumber')
            accountImage = form.cleaned_data.get('image')
            accountZip = Zip.objects.order_by('-id')[0]
            account.zip = accountZip
            account.addressNumber = addressNumber
            account.address = address
            account.accountImage = accountImage
            account.save()
            global username
            username = form.cleaned_data.get('username')
            global password
            password = form.cleaned_data.get('password1')
            return redirect('myAccount-paymentRegister', 0)
    # when function is initially called, empty form is sent via context
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'myAccount/register.html', context)


''' handles payment registration. src variable tells the function where it was called from.
 0 means the user is in the sign up process, 1 means the user is authenticated and is in checkout process,
 2 means the user is updating information in his account '''
def paymentRegister(request, src = '0'):

    # try/except clause to handle wrong type in url parameter
    try:
        context = manufacturerContext(request)

        # gets form data
        form = PaymentForm(data=request.POST)

        # when the user has submitted the form
        if request.method == 'POST':
            if form.is_valid():
                nameOnCard = form.cleaned_data.get('nameOnCard')
                cardNumber = form.cleaned_data.get('cardNumber')
                expirationDate = form.cleaned_data.get('expirationDate')
                CVV = form.cleaned_data.get('CVV')

                # if user is authenticated, he is either in checkout or my account
                if request.user.is_authenticated:
                    currentUser = request.user.id
                    savePayment = PaymentInfo(currentUser, nameOnCard, cardNumber, expirationDate, CVV)
                    savePayment.save()

                    # redirect back to checkout
                    if src == '1':
                        return redirect('checkout-payment')

                    # redirect back to paymentInfo
                    elif src == '2':
                        return redirect('myAccount-paymentInfo')

                # if not, user is in the sign up process
                else:
                    currentUser = Account.objects.latest('id')
                    savePayment = PaymentInfo(currentUser.id, nameOnCard, cardNumber, expirationDate, CVV)
                    savePayment.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                return redirect('homepage-index')

        # when function is initially called, empty form is sent via context
        else:
            form = PaymentForm()
        context['form'] = form
        return render(request, 'myAccount/paymentRegister.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


''' checks if user is authenticated, gets all Order objects that match users id '''
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


''' checks if user is authenticated, renders accountInfo '''
@login_required
def accountInfo(request):
    return render(request, 'myAccount/accountInfo.html')


''' checks if user is authenticated, gets all SearchHistory searches in flat list that match users id,
gets all Product objects that match searches'''
@login_required
def searchHistory(request):
    searchList = []
    context = manufacturerContext(request)
    userId = request.user.id
    searches = SearchHistory.objects.filter(accountId_id=userId).values_list('searchedItem', flat=True)
    for search in searches:
        searchList.append({search: Product.objects.filter(name__icontains=search)})
    context['searched'] = searchList
    context['images'] = ProductImage.objects.all()
    return render(request, 'myAccount/searchHistory.html', context)


''' returns all credit cards linked to current user '''
def paymentInfo(request):
    context = manufacturerContext(request)
    context['users'] = User.objects.all()
    userId = request.user.id
    context['payment'] = PaymentInfo.objects.filter(accountId_id=userId)
    return render(request, 'myAccount/paymentInfo.html', context)


''' returns address linked to current user '''
def getAddress(request):
    for account in Account.objects.all():
        if account.user_id == request.user.id:
            return account.address


''' handles account updates '''
def updateAccount(request):
    context = manufacturerContext(request)

    # when the user has submitted the form
    if request.method == 'POST':

        # gets data and files via POST request
        form = AccountUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            account = user.account
            account.accountImage = form.cleaned_data.get('image')
            account.save()
            return render(request, 'myAccount/accountInfo.html', context)

    # empty form returned initially
    else:
        form = AccountUpdate(instance=request.user)
        context['form'] = form
        return render(request, 'myAccount/updateAccount.html', context)


''' handles Address updates, this is only used when user is in checkout process '''
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
