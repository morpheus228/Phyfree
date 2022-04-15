from django.utils import timezone
import pytz
from rest_framework import serializers
from .models import Order, User


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'title','employer', 'employee', 'status')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['employer', 'title', 'description', 'location', 'price']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['employee']

    def update(self, instance, validated_data):
        instance.employee = validated_data.get("employee", instance.employee)
        instance.activated_at = timezone.now()
        instance.status = 1
        instance.save()

        return instance


class OrderCompleteSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.completed_at = timezone.now()
        instance.status = 2
        instance.save()

        return instance






# class UserDetailSerializer(serializers.ModelSerializer):
#     created_orders = OrderDetailSerializer(many=True)
#
#     class Meta:
#         model = User
#         fields = "__all__"

