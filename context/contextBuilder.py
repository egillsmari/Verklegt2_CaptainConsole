from product.models import Category
from product.models import Platform

def categoriesContext():
    context = {'categories': Category.objects.all().order_by('name')}
    return context

def platformsContext():
    context = {'platforms': Platform.objects.all()}
    return context

def navContext():
    context = {'categories': Category.objects.all(), 'platforms': Platform.objects.all()}
    return context