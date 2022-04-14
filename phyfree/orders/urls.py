from django.urls import path
from .views import *


urlpatterns = [
    path('<int:order_pk>/', OrderDetailView.as_view()),
    path('user/<int:user_pk>/', OrdersByUserListView.as_view()),
    path('user/<int:user_pk>/<str:condition>/', SortedOrdersByUserListView.as_view()),

    path('create/', OrderCreateView.as_view()),
    # path('<int:order_pk>/alter/<str:action>', OrderAlterView.as_view()),

    # path('<int:order_pk>/alter/avail', OrderListView.as_view()),
    # path('<int:order_pk>/alter/activate', OrderListView.as_view()),
    # path('<int:order_pk>/alter/complete', OrderListView.as_view()),
]