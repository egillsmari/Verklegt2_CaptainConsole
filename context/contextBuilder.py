from product.models import Platform
from product.models import Manufacturer
from product.models import Product
from myAccount.models import PaymentInfo


''' helper function that returns context containing all platform objects '''
def platformsContext():
    return {'platforms': Platform.objects.all()}


''' helper function that returns all manufacturer objects, items in cart,
total price of cart and cartId. This context is sent into all html templates so the nav bar
functions properly'''
def manufacturerContext(request):
    context = []
    idcontext = []
    totalPrice = 0
    for item, val in request.session.items():
        if val == 'item':
            for product in Product.objects.all():
                if int(product.id) == int(item):
                    totalPrice += product.price
                    context.append(product)
                    idcontext.append(int(product.id))
    return {'manufacturers': Manufacturer.objects.all(), 'cartItems': context, 'totalPrice':totalPrice, 'cartId':idcontext}


''' helper function that returns all credit card objects  '''
def cardContext(request):
    context = []
    for card in PaymentInfo.objects.all():
        if card.accountId_id == request.user.id:
            context.append(card)
    if context == []:
        context.append('NoCard')
    return context


''' helper function that returns context containing current category, current manufacturer,
all manufacturer objects and all platform objects '''
def allContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.all()}


''' helper function that returns context containing current category, current manufacturer,
all manufacturer objects and all platforms that belong to current manufacturer'''
def narrowContext(category, manufacturer):
    return {'cat': category, 'man': manufacturer, 'manufacturers': Manufacturer.objects.all(), 'platforms': Platform.objects.filter(manufacturer_id=manufacturer).order_by('name')}
