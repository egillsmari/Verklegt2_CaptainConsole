from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold
from context.contextBuilder import cardContext
from product.models import Product, ProductImage
import time


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/showCart.html', context)

def removeItem(request, item):
    try:
        sessionCopy = {k: v for k, v in request.session.items()}
        for key, val in sessionCopy.items():
            if val == 'item' and int(key) == int(item):
                del request.session[key]
        context = manufacturerContext(request)
        return render(request, 'checkout/showCart.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


def shippingMethod(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/shipping.html', context)

def getMethod(request):
    shippMethod = request.GET.get('methodship')
    context = manufacturerContext(request)
    context['shippingMethod'] = shippMethod
    return render(request, 'checkout/confirmation.html', context)

def saveOrder(request, method):
    try:
        sessionCopy = {k: v for k, v in request.session.items()}
        currentUser = request.user.id
        order = Order(accountId_id=currentUser, shippingMethod=method)
        order.save()

        for item, val in sessionCopy.items():
            if val == 'item':
                for product in Product.objects.all():
                    if int(product.id) == int(item):
                        image = _removePhotos(request, product.id)
                        sold = Sold(orderId_id=order.id, name=product.name, price=product.price, image=image)
                        sold.save()
                        del request.session[item]
                        removeItem = Product.objects.get(pk=product.id)
                        removeItem.delete()
        time.sleep(2)
        return redirect('homepage-index')

    except:
        return render(request, '404.html', manufacturerContext(request))


def _removePhotos(request, producId):
    try:
        for image in ProductImage.objects.all():
            if image.product_id == producId:
                retImage = image.productImage
                image.delete()
        return retImage

    except:
        return render(request, '404.html', manufacturerContext(request))

def paymentMethod(request):
    context = manufacturerContext(request)
    context['cards'] = cardContext(request)
    return render(request, 'checkout/paymentMethod.html', context)



