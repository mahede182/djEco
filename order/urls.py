from django.urls import path
from .views import OrderCheckout

urlpatterns = [
    path('checkout/', OrderCheckout.as_view(), name='checkout'),
    path('order-success/', OrderCheckout.order_success, name='order-success')
]