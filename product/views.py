from django.shortcuts import render, redirect
from product.models import Product
from product.models import Platform
from context.contextBuilder import allContext, narrowContext, manufacturerContext
from django.contrib.sessions.backends.db import SessionStore

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request, category, manufacturer):
    if manufacturer == 0:
        context = allContext(category, manufacturer)
        context['products'] = Product.objects.filter(category_id=category).order_by('name')
    else:
        plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
        context = narrowContext(category, manufacturer)
        context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('name')
    return render(request, 'product/index.html', context)


def productFilter(request, category, manufacturer, platform):
    if manufacturer == 0:
        context = allContext(category, manufacturer)
        context['filter'] = platform

    else:
        context = narrowContext(category, manufacturer)
    context['products'] = Product.objects.filter(category_id=category, platform_id=platform).order_by('name')
    return render(request, 'product/index.html', context)



def productSort(request, category, manufacturer, sort):
    context = narrowContext(category, manufacturer)
    plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)


def productPlatform():
    pass


def productRange():
    pass

def productInfo(request, productid):
    context = manufacturerContext(request)
    context['products'] = Product.objects.filter(id=productid)
    return render(request, 'productInfo/index.html', context)


def addToCart(request, productid):
    request.session[productid] = 'item'
    return redirect('homepage-index')

def emptyCart(request):
    for key, val in request.session.items():
        if val == 'item':
            del request.session[key]
    return redirect('homepage-index')


