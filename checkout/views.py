from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold
from myAccount.models import PaymentInfo
from django.contrib.auth.models import User
from context.contextBuilder import cardContext
from product.models import Product


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/showCart.html', context)

def shippingMethod(request):
    context = manufacturerContext(request)
    currentUser = request.user.id
    shippMethod = request.GET.get('method')
    for item, val in request.session.items():
        if val == 'item':
            for product in Product.objects.all():
                if int(product.id) == int(item):
                    order = Order(accountId_id=currentUser, productId_id=product.id, shippingMethod=shippMethod)
                    order.save()
    return render(request, 'checkout/shipping.html', context)

def paymentMethod(request):
    context = manufacturerContext(request)
    context['cards'] = cardContext(request)
    return render(request, 'checkout/paymentMethod.html', context)

def confirmation(request):
    for key, val in request.session.items():
        if val == 'item':
            del request.session[key]
    context = manufacturerContext(request)
    return render(request, 'checkout/confirmation.html', context)

