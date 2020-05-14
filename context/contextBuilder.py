from product.models import Platform
from product.models import Manufacturer
from product.models import Product
from myAccount.models import PaymentInfo



def platformsContext():
    return {'platforms': Platform.objects.all()}

def manufacturerContext(request):
    context = []
    totalPrice = 0
    for item, val in request.session.items():
        if val == 'item':
            for product in Product.objects.all():
                if int(product.id) == int(item):
                    totalPrice += product.price
                    context.append(product)
    return {'manufacturers': Manufacturer.objects.all(), 'cartItems': context, 'totalPrice':totalPrice}

def cardContext(request):
    context = []
    for card in PaymentInfo.objects.all():
        if card.accountId_id == request.user.id:
            context.append(card)
    if context == []:
        context.append('NoCard')
    return context



def allContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.all()}

def narrowContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.filter(manufacturer_id=manufacturer).order_by('name')}
