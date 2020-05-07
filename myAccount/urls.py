from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.accountInfo, name='accountInfo'),
    path('/register', views.register, name='register'),
    path('/seePurchasehistory', views.seePurchasehistory, name='seePurchasehistory'),
    path('/login', LoginView.as_view(template_name='myAccount/login.html'), name='login'),
    path('/logout', LogoutView.as_view(next_page='homepage-index'), name='logout'),
]