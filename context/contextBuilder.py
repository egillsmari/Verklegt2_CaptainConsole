from product.models import Category
from product.models import Platform
from product.models import Manufacturer

def categoriesContext():
    context = {'categories': Category.objects.all().order_by('name')}
    return context

def platformsContext():
    context = {'platforms': Platform.objects.all()}
    return context

def manufacturerContext():
    context = {'manufacturers': Manufacturer.objects.all()}
    return context

def navContext():
    context = {'categories': Category.objects.all(), 'platforms': Platform.objects.all()}
    return context