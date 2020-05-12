from product.models import Category
from product.models import Platform
from product.models import Manufacturer
from product.models import Product


def platformsContext():
    return {'platforms': Platform.objects.all()}

def manufacturerContext(request):
    context = []
    for item in request.session.keys():
        for product in Product.objects.all():
            if int(product.id) == int(item):
                context.append(product.name)
    return {'manufacturers': Manufacturer.objects.all(), 'cartItems': context}

def allContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.all()}

def narrowContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.filter(manufacturer_id=manufacturer).order_by('name')}
