from django.urls import path
from .views import OrderListView, OrderDetailView, OrderItemListView, OrderItemDetailView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order_items/', OrderItemListView.as_view(), name='order-item-list'),
    path('order_items/<int:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),
]
