from django.shortcuts import render, redirect
from context.contextBuilder import manufacturerContext

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def showCart(request):
    context = manufacturerContext(request)
    context['test'] = request.session
    return render(request, 'checkout/showCart.html', context)

def emptyCart(request):
    request.session.flush()
    for key, val in request.session.items():
        if val == 'item':
            del request.session[key]
    return redirect('homepage-index')

