from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class OrderDetailView(APIView):
    def get(self, request, order_pk):
        order = Order.objects.get(id=order_pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    def delete(self, request, order_pk):
        instance = Order.objects.get(id=order_pk)
        instance.delete()
        return Response("Successfully deleted")


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
        order.is_valid(raise_exception=True)
        order.save()

        return Response({'post': order.data}, status=201)


class OrderAlterView(APIView):
    ALLOWED_ALTERS = ['activate', 'complete']

    def put(self, request, *args, **kwargs):
        order_pk = kwargs.get('order_pk', None)
        action = kwargs.get('action', None)

        if (not order_pk) or (action not in self.ALLOWED_ALTERS):
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Order.objects.get(id=order_pk)
        except:
            return Response({"error": "This user id doesn't exist"})

        if kwargs["action"] == "activate":
            serializer = OrderActivateSerializer(data=request.data, instance=instance)

        elif kwargs["action"] == "complete":
            serializer = OrderCompleteSerializer(data=request.data, instance=instance)

        serializer.is_valid()
        serializer.save()

        return Response({"put": OrderDetailSerializer(instance).data})



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