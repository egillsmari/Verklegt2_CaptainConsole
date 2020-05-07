from django.urls import path
from . import views

urlpatterns = [
    path('<int:manufacturer>/', views.index, name='consoles-index'),
    path('<int:manufacturer>/<int:platform>', views.productView, name='consoles-productView')
]