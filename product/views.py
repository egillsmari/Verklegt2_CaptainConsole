from django.shortcuts import render
from product.models import Product
from context.contextBuilder import platformsContext, manufacturerContext

# Create your views here.
def index(request, category, manufacturer):
    context = platformsContext()
    if manufacturer == 0:
        context['product'] = Product.objects.filter(category_id=category).order_by('name')
    else:
        context['product'] = Product.objects.filter(category_id=category, manufacturer_id=manufacturer).order_by('name')
    return render(request, 'product/index.html', context)

def productSort():
    pass

def productFilter():
    pass

def productRange():
    pass