from django.shortcuts import render
from product.models import Product
from context.contextBuilder import manufacturerContext


# Create your views here.
def index(request):
    context = manufacturerContext()
    context['products'] = Product.objects.all().order_by('category_id')
    return render(request, 'homepage/index.html', context)
