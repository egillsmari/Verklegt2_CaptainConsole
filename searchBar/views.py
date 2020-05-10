from django.shortcuts import render
from product.models import Product
from myAccount.models import SearchHistory
from context.contextBuilder import manufacturerContext




# Create your views here.
def index(request):
    context = manufacturerContext()
    query = request.GET.get('q')
    context['products'] = Product.objects.filter(name__icontains=query)
    if request.user.is_authenticated:
        current_user = request.user.id
        history = SearchHistory(searchedItem=query, accountId_id=current_user)
        history.save()



    return render(request, 'searchBar/index.html', context)

