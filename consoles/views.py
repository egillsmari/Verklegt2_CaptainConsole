from django.shortcuts import render
from product.models import Product
from context.contextBuilder import platformsContext

# Create your views here.
def index(request, platform):
    context = platformsContext()
    if platform == 0:
        context['consoles'] =  Product.objects.filter(category_id=2).order_by('name')
    else:
        context['consoles'] = Product.objects.filter(category_id=2, platform_id=platform).order_by('name')
    return render(request, 'consoles/index.html', context)

