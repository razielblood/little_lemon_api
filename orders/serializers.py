from rest_framework import serializers
from orders.models import Order, OrderItem
from menu.models import MenuItem


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = serializers.StringRelatedField()
    menuitem_id = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), write_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = OrderItem
        fields = ["id", "order", "menuitem", "menuitem_id", "quantity", "unit_price", "price"]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(write_only=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "user", "user_id", "delivery_crew", "status", "total", "date", "order_items"]
