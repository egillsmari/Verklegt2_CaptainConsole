from product.models import Category

def categoriesContext():
    context = {'categories': Category.objects.all().order_by('name')}
    return context

def platformsContext():
    context = {'platforms': }