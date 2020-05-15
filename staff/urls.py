from django.urls import path
from . import views

urlpatterns = [
    path('productInfo/', views.addProduct, name='staff-index'),
    path('productImage/', views.addImage, name='staff-addImage')
]