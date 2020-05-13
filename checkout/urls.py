from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='checkout-index'),
    path('cart/', views.showCart, name='checkout-cart'),
    path('payment/', views.paymentMethod, name='checkout-payment'),
    path('shipping/', views.shippingMethod, name='checkout-shipping'),
    path('confirmation/', views.saveOrder, name='checkout-saveOrder')
]