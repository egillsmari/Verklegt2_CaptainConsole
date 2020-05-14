
from django.shortcuts import render
from product.models import Product
from product.models import ProductImage
from context.contextBuilder import manufacturerContext

# Create your views here.

def index(request):
    context = manufacturerContext(request)
    context['products'] = Product.objects.all().order_by('category_id')
    context['images'] = ProductImage.objects.all()
    return render(request, 'homepage/index.html', context)

def contacUs(request, sentQ):
    try:
        context = manufacturerContext(request)
        context['sentQ'] = sentQ
        return render(request, 'contactUs/intex.html', context)

    except:
        return render(request, '404.html', manufacturerContext(request))
