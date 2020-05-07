from django.urls import path
from . import views

urlpatterns = [
    path('<int:manufacturer>/', views.index, name='consoles-index')
]