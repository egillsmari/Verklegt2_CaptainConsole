from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.accountInfo, name='accountInfo'),
    path('registerLocation', views.locationRegister, name='registerLocation'),
    path('register', views.register, name='myAccount-register'),
    path('seePurchasehistory', views.seePurchasehistory, name='seePurchasehistory'),
    path('login', LoginView.as_view(template_name='myAccount/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='homepage-index'), name='logout'),
    path('paymentRegister/<int:src>', views.paymentRegister, name='myAccount-paymentRegister'),
    path('paymentInfo', views.paymentInfo, name='myAccount-paymentInfo'),
    path('purchaseHistory', views.seePurchasehistory, name='myAccount-purchaseHistory'),
    path('searchHistory', views.searchHistory, name='myAccount-searchHistory'),
    path('accountEdit', views.updateAccount, name='myAccount-updateAccount'),
    path('addressEdit', views.updateAddress, name='myAccount-updateAddress')
]