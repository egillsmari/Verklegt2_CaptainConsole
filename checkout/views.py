from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext
from checkout.models import Order, Sold
from context.contextBuilder import cardContext
from product.models import Product, ProductImage
import time


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

'''returns the context to build user cart and images'''
def showCart(request):
    context = manufacturerContext(request)
    context['images'] = ProductImage.objects.all()
    return render(request, 'checkout/showCart.html', context)

''' Removes the requested item from the cart. Creates a copy of
    of the session(session can't be iterated trough with when rendering) '''
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

'''User sent to Shipping method page'''
def shippingMethod(request):
    context = manufacturerContext(request)
    return render(request, 'checkout/shipping.html', context)

'''Get the choosen shipping method from user (gets value from button click)'''
def getMethod(request):
    shippMethod = request.GET.get('methodship')
    context = manufacturerContext(request)
    context['shippingMethod'] = shippMethod
    return render(request, 'checkout/confirmation.html', context)

''' Function creates a Order for user. Adds the product to the sold table and
    removes it from product table. Deletes product images from image table and only adds
    one photo to sold table. When order is received, page redirects to homepage after 1 sec '''
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
        time.sleep(1)
        return redirect('homepage-index')

    except:
        return render(request, '404.html', manufacturerContext(request))

'''removes the photos for the product with corrosponding product id'''
def _removePhotos(request, producId):
    retImage = ''
    try:
        for image in ProductImage.objects.all():
            if image.product_id == producId:
                retImage = image.productImage
                image.delete()
        return retImage
    except:
        return render(request, '404.html', manufacturerContext(request))

''' shows the user his current card'''
def paymentMethod(request):
    context = manufacturerContext(request)
    context['cards'] = cardContext(request)
    return render(request, 'checkout/paymentMethod.html', context)



