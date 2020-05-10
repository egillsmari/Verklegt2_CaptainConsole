from django.shortcuts import render
from product.models import Product
from product.models import Platform
from context.contextBuilder import allContext, narrowContext

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
    context = narrowContext(category, manufacturer)
    context['products'] = Product.objects.filter(category_id=category, platform_id=platform).order_by('name')
    return render(request, 'product/index.html', context)

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

def productRange(request, category, manufacturer):
    context = narrowContext(category, manufacturer)
    plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
    fromRange = request.GET.get('from')
    toRange = request.GET.get('to')
    context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat, price__gte=fromRange, price__lte=toRange).order_by('name')
    return render(request, 'product/index.html', context)
