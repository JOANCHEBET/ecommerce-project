
from django.urls import path
from .views import ProductList, OrderList, api_root
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', api_root),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
]
