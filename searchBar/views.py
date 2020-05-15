from django.shortcuts import render, redirect
from product.models import Product
from myAccount.models import SearchHistory
from context.contextBuilder import manufacturerContext

# Create your views here.
'''Gets value from textfield, search through all names in products and returns right products'''
def index(request):
    context = manufacturerContext(request)
    query = request.GET.get('q')
    context['products'] = Product.objects.filter(name__icontains=query)
    if context['products'].exists():
        if query == ' ' or query == '':
            return redirect('homepage-index')
        elif request.user.is_authenticated:
            current_user = request.user.id
            history = SearchHistory(searchedItem=query, accountId_id=current_user)
            history.save()
        return render(request, 'searchBar/index.html', context)
    else:
        return render(request, 'searchBar/noItem.html')

