from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='checkout-index'),
    path('cart/', views.showCart, name='checkout-cart'),
    path('payment/', views.paymentMethod, name='checkout-payment'),
    path('shipping/', views.shippingMethod, name='checkout-shipping'),
    path('confirmation/<method>', views.saveOrder, name='checkout-saveOrder'),
    path('shipmentMethod/', views.getMethod, name='checkout-getMethod'),
    path('rem<item>', views.removeItem, name='checkout-remove')
]