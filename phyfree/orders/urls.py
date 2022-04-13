from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
]