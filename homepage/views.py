from django.shortcuts import render
from product.models import Product
from context.contextBuilder import navHelper


# Create your views here.
def index(request):
    context = navHelper()
    context['products'] = Product.objects.all().order_by('category')
    return render(request, 'homepage/index.html', context)
