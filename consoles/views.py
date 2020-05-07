from django.shortcuts import render
from product.models import Product
from context.contextBuilder import platformsContext, manufacturerContext

# Create your views here.
def index(request, manufacturer):
    context = platformsContext()
    if manufacturer == 0:
        context['consoles'] = Product.objects.filter(category_id=2).order_by('name')
    else:
        context['consoles'] = Product.objects.filter(category_id=2, manufacturer_id=manufacturer).order_by('name')
    return render(request, 'consoles/index.html', context)

def productView(request, platform):
    pass

