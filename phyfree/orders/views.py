from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class OrderDetailView(APIView):
    def get(self, request, order_pk):
        order = Order.objects.get(id=order_pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)


class OrdersByUserListView(APIView):
    def get(self, request, user_pk):
        orders = Order.objects.filter(employer__exact=user_pk) | Order.objects.filter(employee__exact=user_pk)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class SortedOrdersByUserListView(APIView):
    def get(self, request, user_pk, condition):
        if condition == 'published':
            orders = Order.objects.filter(employer__exact=user_pk, status__exact=0)

        elif condition == 'available':
            orders = Order.objects.filter(status__exact=0).exclude(employer__exact=user_pk)

        elif condition == 'active':
            orders = Order.objects.filter(status__exact=1)
            orders = orders.filter(employer__exact=user_pk) | orders.filter(employee__exact=user_pk)

        elif condition == 'completed':
            orders = Order.objects.filter(status__exact=2)
            orders = orders.filter(employer__exact=user_pk) | orders.filter(employee__exact=user_pk)

        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderCreateView(APIView):
    def post(self, request):
        order = OrderCreateSerializer(data=request.data)
        if order.is_valid():
                order.status = 0
                order.save()
                return Response(status=201)

        return Response(status=400)


# class OrderAlterView(APIView):
#     def post(self, request, order_pk, action):
#         if action == "activate":
#             pass
#
#         elif action == "complete":
#             pass
#
#         elif action == "delete":
#             pass
#
#         order = OrderCreateSerializer(data=request.data)
#         if order.is_valid():
#                 order.status = 0
#                 order.save()
#                 return Response(status=201)
#
#         return Response(status=400)

# class UserDetailView(APIView):
#     def get(self, request, pk):
#         user = User.objects.get(id=pk)
#         serializer = UserDetailSerializer(user)
#         return Response(serializer.data)