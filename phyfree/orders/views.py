from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)


class OrderCreateView(APIView):
    def post(self, request):
        order = OrderCreateSerializer(data=request.data)
        if order.is_valid():
            order.status = "CREATED"
            order.save()
            return Response(status=201)

        return Response(status=404)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)