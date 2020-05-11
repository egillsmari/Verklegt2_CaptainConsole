from django.shortcuts import render
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

<<<<<<< HEAD

=======
>>>>>>> origin/master
def productFilter(request, category, manufacturer, platform):
    if manufacturer == 0:
        context = allContext(category, manufacturer)
        context['filter'] = platform

    else:
        context = narrowContext(category, manufacturer)
    context['products'] = Product.objects.filter(category_id=category, platform_id=platform).order_by('name')
    return render(request, 'product/index.html', context)

<<<<<<< HEAD

def productSort(request, category, manufacturer, sort):
    context = narrowContext(category, manufacturer)
    plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)

def productSort(request, category, manufacturer, sort):
    context = narrowContext(category, manufacturer)
    plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)

    if sort == 0:
        context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('price')
    elif sort == 1:
        context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('-price')
    elif sort == 2:
        pass
    elif sort == 3:
        context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('releaseDate')
    return render(request, 'product/index.html', context)



def productPlatform():
    pass


def productRange():
    pass

def productRange(request, category, manufacturer):
    context = narrowContext(category, manufacturer)
    plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
=======
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
                pass
            elif sort == 3:
                context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('releaseDate')
        else:
            if sort == 0:
                context['products'] = Product.objects.filter(category_id=category).order_by('price')
            elif sort == 1:
                context['products'] = Product.objects.filter(category_id=category).order_by('-price')
            elif sort == 2:
                pass
            elif sort == 3:
                context['products'] = Product.objects.filter(category_id=category).order_by('releaseDate')
    else:
        context = narrowContext(category, manufacturer)
        plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
        if sort == 0:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('price')
        elif sort == 1:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('-price')
        elif sort == 2:
            pass
        elif sort == 3:
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('releaseDate')
    return render(request, 'product/index.html', context)


def productRange(request, category, manufacturer, filter):
>>>>>>> origin/master
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
<<<<<<< HEAD

def productInfo(request, productid):
    context = manufacturerContext()
    context['products'] = Product.objects.filter(id=productid)
    return render(request, 'productInfo/index.html', context)

=======
>>>>>>> origin/master
