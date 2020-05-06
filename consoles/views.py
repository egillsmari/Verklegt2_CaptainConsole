from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request, type):
    if type == 'all':
        context = {'consoles': Product.objects.all().order_by('name')}
    else:
        context = {'consoles': Product.objects.filter(type=type).order_by('name')}
    return render(request, 'consoles/index.html', context)

