from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage-index'),
    path('contactUs/<int:sentQ>', views.contacUs, name='contactUs-index')
]