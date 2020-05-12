from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='checkout-index'),
    path('cart/', views.showCart, name='checkout-cart'),
    path('empty/', views.emptyCart, name='checkout-emptyCart')

]