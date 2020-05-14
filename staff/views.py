from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    return render(request, 'staff/add.html')