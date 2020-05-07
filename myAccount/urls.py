from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.register, name='myAccount-index'),
    path('login', LoginView.as_view(template_name='myAccount/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]