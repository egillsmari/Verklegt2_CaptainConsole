from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('<category>/<manufacturer>', views.index, name='product-index'),
    path('info/prod/<product_id>', views.productInfo, name='product-productInfo'),
    path('<category>/<manufacturer>/filter/<platform>', views.productFilter, name='product-productFilter'),
    path('<category>/<manufacturer>/sort/<filter>/<sort>', views.productSort, name='product-productSort'),
    path('<category>/<manufacturer>/range/<filter>', views.productRange, name='product-productRange'),
    path('added/cart/<product_id>', views.addToCart, name='product-addToCart'),
    path('empty/', views.emptyCart, name='checkout-emptyCart')

]

