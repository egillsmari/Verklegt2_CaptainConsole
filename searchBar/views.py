from django.http import JsonResponse
from product.models import Product




# Create your views here.
def index(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image
        }for x in Product.objects.filter(name__icontains=searchFilter)]
        #  products = list(Product.objects.filter(name__icontains=searchFilter).values())
        return JsonResponse({'data': products})