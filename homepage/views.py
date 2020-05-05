from django.shortcuts import render
from product.models import Product


# Create your views here.
def index(request):
    context = {'products': Product.objects.all().order_by('category')}
    return render(request, 'homepage/index.html', context)
