from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('<int:category>/<int:manufacturer>', views.index, name='product-index'),
<<<<<<< HEAD
    path('<int:category>/<int:manufacturer>/<int:platform>', views.productFilter, name='product-productFilter'),
    path('<int:category>/<int:manufacturer>/<int:sort>', views.productSort, name='product-productSort'),
    path('<int:category>/<int:manufacturer>/<int:range>', views.productRange, name='product-productRange'),
    path('<int:category>/<int:manufacturer>/filter/<int:platform>', views.productFilter, name='product-productFilter'),
    path('<int:category>/<int:manufacturer>/sort/<int:sort>', views.productSort, name='product-productSort'),
    path('<int:category>/<int:manufacturer>/range', views.productRange, name='product-productRange'),
    path('<int:productid>', views.productInfo, name='productInfo-index')

=======
    path('<int:category>/<int:manufacturer>/filter/<int:platform>', views.productFilter, name='product-productFilter'),
    path('<int:category>/<int:manufacturer>/sort/<int:filter>/<int:sort>', views.productSort, name='product-productSort'),
    path('<int:category>/<int:manufacturer>/range/<int:filter>', views.productRange, name='product-productRange')
>>>>>>> origin/master
]

