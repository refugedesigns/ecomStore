from django.urls import path
from .views import storeView,cartView,checkoutView 

urlpatterns = [
    path('', storeView, name='store'),
    path('cart/', cartView, name='cart'),
    path('checkout/', checkoutView, name='checkout'),
]