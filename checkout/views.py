from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold
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
    return render(request, 'checkout/shipping.html', context)

def saveOrder(request):
    sessionCopy = {k: v for k, v in request.session.items()}
    context = manufacturerContext(request)
    currentUser = request.user.id
    shippMethod = request.GET.get('methodship')
    for item, val in sessionCopy.items():
        if val == 'item':
            for product in Product.objects.all():
                if int(product.id) == int(item):
                    order = Order(accountId_id=currentUser, productId_id=product.id, shippingMethod=shippMethod)
                    order.save()
                    sold = Sold(orderId_id=order.id)
                    sold.save()
                    del request.session[item]
                    removeItem = Product.objects.get(pk=product.id)
                    removeItem.delete()
    return render(request, 'checkout/confirmation.html', context)

def paymentMethod(request):
    context = manufacturerContext(request)
    context['cards'] = cardContext(request)
    return render(request, 'checkout/paymentMethod.html', context)

def confirmation(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/confirmation.html', context)
