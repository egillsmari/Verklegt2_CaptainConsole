from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/showCart.html', context)

def shippingMethod(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/shipping.html', context)

def paymentMethod(request):
    context = manufacturerContext(request)
    return render(request, '')

