from django.urls import path
from . import views

urlpatterns = [
    path('<int:platform>/', views.index, name='games-index'),
]