from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold
from context.contextBuilder import cardContext
from product.models import Product
import time


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/showCart.html', context)

def shippingMethod(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/shipping.html', context)

def getMethod(request):
    shippMethod = request.GET.get('methodship')
    context = manufacturerContext(request)
    context['shippingMethod'] = shippMethod
    return render(request, 'checkout/confirmation.html', context)

def saveOrder(request, method):
    sessionCopy = {k: v for k, v in request.session.items()}
    context = manufacturerContext(request)
    currentUser = request.user.id
    order = Order(accountId_id=currentUser, shippingMethod=method)
    order.save()
    for item, val in sessionCopy.items():
        if val == 'item':
            for product in Product.objects.all():
                if int(product.id) == int(item):
                    sold = Sold(orderId_id=order.id, name=product.name, price=product.price, image=product.image)
                    sold.save()
                    del request.session[item]
                    removeItem = Product.objects.get(pk=product.id)
                    removeItem.delete()
    time.sleep(1)
    return redirect('homepage-index')

def paymentMethod(request):
    context = manufacturerContext(request)
    context['cards'] = cardContext(request)
    return render(request, 'checkout/paymentMethod.html', context)



