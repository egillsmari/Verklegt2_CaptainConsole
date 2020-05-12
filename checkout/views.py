from django.shortcuts import render
from context.contextBuilder import manufacturerContext

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    context['test'] = request.session
    return render(request, 'checkout/showCart.html', context)
