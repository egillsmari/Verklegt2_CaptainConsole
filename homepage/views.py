from django.shortcuts import render
from product.models import Product
from product.models import ProductImage
from context.contextBuilder import manufacturerContext

# Create your views here.
''' calls helper function that returns all manufacturer objects,
 adds all product objects and all image objects. Sends context to
 homepage index and renders'''
def index(request):
    context = manufacturerContext(request)
    context['products'] = Product.objects.all().order_by('category_id')
    context['images'] = ProductImage.objects.all()
    return render(request, 'homepage/index.html', context)


''' calls helper function that returns all manufacturer objects, adds sentQ to 
context and renders contactUs index'''
def contacUs(request, sentQ):
    try:
        context = manufacturerContext(request)
        context['sentQ'] = sentQ
        return render(request, 'contactUs/intex.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))


''' below functions all handle various errors, each function renders
appropriate error page'''
def bad_request(request, exception):
    return render(request, '400.html', manufacturerContext(request))

def permission_denied(request, exception):
    return render(request, '403.html', manufacturerContext(request))

def page_not_found(request, exception):
    return render(request, '404.html', manufacturerContext(request))

def server_error(request):
    return render(request, '500.html', manufacturerContext(request))
