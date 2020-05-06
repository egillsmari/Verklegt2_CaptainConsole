from django.shortcuts import render
from product.models import Product
from context.contextBuilder import platformsContext

# Create your views here.
def index(request, platform):
    context = platformsContext()
    if platform == 'all':
        context['games'] = Product.objects.filter(category_id=1).order_by('name')
    else:
        context['games'] = Product.objects.filter(category_id=1, platform_id=platform).order_by('name')
    return render(request, 'games/index.html', context)