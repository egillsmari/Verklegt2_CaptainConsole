from django.shortcuts import render, redirect
from product.models import Product
from product.models import Platform
from product.models import ProductImage
from context.contextBuilder import allContext, narrowContext, manufacturerContext


# Create your views here.
''' handles product index page, sends context depending on category and manufacturer selection in nav bar '''
def index(request, category, manufacturer):

    # try/except clause to handle wrong types in url params
    try:

        # See all selected in nav bar, context contains all categories, all manufacturers and all products
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            context['products'] = Product.objects.filter(category_id=category).order_by('name')

        # Some manufacturer selected in nav bar
        else:

            # context contains only platforms and products belonging to selected manufacturer and category
            plat = Platform.objects.filter(manufacturer_id=manufacturer).values_list('id', flat=True)
            context = narrowContext(category, manufacturer)
            context['products'] = Product.objects.filter(category_id=category, platform_id__in=plat).order_by('name')

        # all images sent with context
        context['images'] = ProductImage.objects.all()
        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


''' handles product filtering, returns context in regard to filter selection '''
def productFilter(request, category, manufacturer, platform):
    try:
        # user chose to see all items
        if manufacturer == '0':
            context = allContext(category, manufacturer)
            context['filter'] = platform

        # user has selected manufacturer
        else:
            context = narrowContext(category, manufacturer)

        # products belonging to selected platform filter added to context
        context['products'] = Product.objects.filter(category_id=category, platform_id=platform).order_by('name')
        context['images'] = ProductImage.objects.all()

        return render(request, 'product/index.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


''' handles product sorting, url parameter indicates sorting type, multiple if/else statements with
differing contexts are there to guarantee that the user always has correct items in dropdown lists in regard to selected 
 category and manufacturer and always has correct products'''
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


''' handles product price range filtering, uses GET request to access input values and filters products
 manufacturer and filter params are there to indicate which filters the user has already chosen'''
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


''' handles context for productInfo page '''
def productInfo(request, product_id):
    context = manufacturerContext(request)
    context['products'] = Product.objects.filter(id=product_id)
    context['images'] = ProductImage.objects.all()
    return render(request, 'productInfo/index.html', context)


''' finds right object in current user session and adds the object to temp list (cart) '''
def addToCart(request, product_id):
    try:
        request.session[int(product_id)] = 'item'
        return redirect('homepage-index')
    except:
        return render(request, '404.html', manufacturerContext(request))


''' clears temp list (cart) and objects '''
def emptyCart(request):
    sessionCopy = { k : v for k,v in request.session.items()}
    for key, val in sessionCopy.items():
        if val == 'item':
            del request.session[key]
    return redirect('homepage-index')


