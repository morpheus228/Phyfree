from rest_framework import serializers
from .models import Order, User


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'title', 'description', 'price', 'employer', 'employee')


class OrderDetailSerializer(serializers.ModelSerializer):
    employer = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Order
        exclude = ["id"]


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['employer', 'title', 'description', 'location', 'price']


class UserDetailSerializer(serializers.ModelSerializer):
    created_orders = OrderDetailSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"

