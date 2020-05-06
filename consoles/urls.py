from django.urls import path
from . import views

urlpatterns = [
    path('/<str:type>/', views.index, name='consoles-index')
]