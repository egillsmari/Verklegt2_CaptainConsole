from django.shortcuts import render, redirect
from django.http import Http404
from product.models import Product
from product.models import Platform
from product.models import ProductImage
from context.contextBuilder import allContext, narrowContext, manufacturerContext


# Create your views here.
'''VANTAR COMMENT'''
def index(request, category, manufacturer):
    try:
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            context['products'] = Product.objects.filter(category_id=category).order_by('name')
        else:
            plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
            context = narrowContext(category, manufacturer)
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('name')
        context['images'] = ProductImage.objects.all()
        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


'''Catch category, manufacturer and platform Id for more detailed search'''
def productFilter(request, category, manufacturer, platform):
    try:
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            context['filter'] = platform

        else:
            context = narrowContext(category, manufacturer)
        context['products'] = Product.objects.filter(category_id=category, platform_id=platform).order_by('name')
        context['images'] = ProductImage.objects.all()

        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


'''VANTAR COMMENT'''
def productSort(request, category, manufacturer, filter, sort):
    try:
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            if filter != '0':
                context['filter'] = filter
                if sort == '0':
                    context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('price')
                elif sort == '1':
                    context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('-price')
                elif sort == '2':
                    context['products'] = Product.objects.filter(category_id=category, platform_id=filter).order_by('releaseDate')
            else:
                if sort == '0':
                    context['products'] = Product.objects.filter(category_id=category).order_by('price')
                elif sort == '1':
                    context['products'] = Product.objects.filter(category_id=category).order_by('-price')
                elif sort == '2':
                    context['products'] = Product.objects.filter(category_id=category).order_by('releaseDate')
        else:
            context = narrowContext(category, manufacturer)
            plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
            if sort == '0':
                context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('price')
            elif sort == '1':
                context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('-price')
            elif sort == '2':
                context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('releaseDate')

        context['images'] = ProductImage.objects.all()
        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


'''VANTAR COMMENT'''
def productRange(request, category, manufacturer, filter):
    try:
        fromRange = request.GET.get('from')
        toRange = request.GET.get('to')
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            if filter != '0':
                context['filter'] = filter
                context['products'] = Product.objects.filter(category_id=category, platform_id=filter, price__gte=fromRange, price__lte=toRange)
            else:
                context['products'] = Product.objects.filter(category_id=category, price__gte=fromRange, price__lte=toRange).order_by('name')
        else:
            context = narrowContext(category, manufacturer)
            plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat, price__gte=fromRange,
                                                         price__lte=toRange).order_by('name')

        context['images'] = ProductImage.objects.all()
        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


'''Filter product id retun right product object'''
def productInfo(request, product_id):
    context = manufacturerContext(request)
    context['products'] = Product.objects.filter(id=product_id)
    context['images'] = ProductImage.objects.all()
    return render(request, 'productInfo/index.html', context)


'''Find right object in current user session and adds the object to temp list'''
def addToCart(request, product_id):
    try:
        request.session[int(product_id)] = 'item'
        return redirect('homepage-index')
    except:
        return render(request, '404.html', manufacturerContext(request))


'''Clears temp list og objects'''
def emptyCart(request):
    sessionCopy = { k : v for k,v in request.session.items()}
    for key, val in sessionCopy.items():
        if val == 'item':
            del request.session[key]
    return redirect('homepage-index')


