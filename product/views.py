from django.shortcuts import render, redirect
from product.models import Product
from product.models import Platform
from context.contextBuilder import allContext, narrowContext, manufacturerContext


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

def productPlatform():
    pass


def productSort(request, category, manufacturer, filter, sort):
    if manufacturer == 0:
        context = allContext(category, manufacturer)
        if filter != 0:
            context['filter'] = filter
            if sort == 0:
                context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('price')
            elif sort == 1:
                context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('-price')
            elif sort == 2:
                context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('releaseDate')
        else:
            if sort == 0:
                context['products'] = Product.objects.filter(category_id=category).order_by('price')
            elif sort == 1:
                context['products'] = Product.objects.filter(category_id=category).order_by('-price')
            elif sort == 2:
                context['products'] = Product.objects.filter(category_id=category).order_by('releaseDate')
    else:
        context = narrowContext(category, manufacturer)
        plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
        if sort == 0:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('price')
        elif sort == 1:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('-price')
        elif sort == 2:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('releaseDate')
    return render(request, 'product/index.html', context)


def productRange(request, category, manufacturer, filter):
    fromRange = request.GET.get('from')
    toRange = request.GET.get('to')
    if manufacturer == 0:
        context = allContext(category, manufacturer)
        if filter != 0:
            context['filter'] = filter
            context['products'] = Product.objects.filter(category_id=category, platform_id=filter, price__gte=fromRange, price__lte=toRange)
        else:
            context['products'] = Product.objects.filter(category_id=category, price__gte=fromRange, price__lte=toRange).order_by('name')
    else:
        context = narrowContext(category, manufacturer)
        plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
        context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat, price__gte=fromRange,
                                                     price__lte=toRange).order_by('name')
    return render(request, 'product/index.html', context)


def productInfo(request, productid):
    context = manufacturerContext(request)
    context['products'] = Product.objects.filter(id=productid)
    return render(request, 'productInfo/index.html', context)


def addToCart(request, productid):
    for key in request.session.keys():
        if key == productid:
            return 0
        else:
            request.session[productid] = 'item'
            return redirect('homepage-index')

def emptyCart(request):
    sessionCopy = { k : v for k,v in request.session.items()}
    for key, val in sessionCopy.items():
        if val == 'item':
            del request.session[key]
    return redirect('homepage-index')


