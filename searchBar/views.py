
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from product.models import Product




# Create your views here.
def index(request):
    query = request.GET.get('q')
    object_list = {'products': Product.objects.filter(name__icontains=query)}
    return render(request, 'searchBar/index.html', object_list)

