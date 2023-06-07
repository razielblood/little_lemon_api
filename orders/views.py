from decimal import Decimal

from django.db import transaction
from django.forms.models import model_to_dict
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer
from menu.serializers import MenuItemSerializer
from orders.models import Order, OrderItem
from orders.serializers import OrderItemSerializer, OrderSerializer


# Create your views here.
class ListCreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        user = request.user

        if user.is_superuser or user.groups.filter(name="Manager").exists():
            orders = Order.objects.all()
        elif user.groups.filter(name="Delivery Crew").exists():
            orders = Order.objects.filter(delivery_crew=user)
        else:
            orders = Order.objects.filter(user=user)

        serialized_orders = OrderSerializer(orders, many=True)

        return Response(serialized_orders.data)

    def post(self, request: HttpRequest):
        user = request.user
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            return Response({"message": "The cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        cart_items_deserialized = CartSerializer(cart_items, many=True).data

        try:
            with transaction.atomic():
                order_total = sum(map(lambda x: Decimal(x.get("price")), cart_items_deserialized))

                # Create order
                order = Order.objects.create(user=user, total=order_total)
                # Create items
                for cart_item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        menuitem=cart_item.menuitem,
                        quantity=cart_item.quantity,
                        unit_price=cart_item.unit_price,
                        price=cart_item.price,
                    )
                # Delete cart
                cart_items.delete()
        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(model_to_dict(order), status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyOrderView(APIView):
    def get(self, request: HttpRequest, order_id: int):
        user = request.user

        order = get_object_or_404(Order, id=order_id)

        if not (user.is_superuser or user.groups.filter(name="Manager").exists() or user.id == order.user.id):
            return Response({"error": "Not Authorized"}, status=status.HTTP_403_FORBIDDEN)

        order_items = OrderItem.objects.filter(order=order)

        order_items_deserialized = OrderItemSerializer(order_items, many=True).data

        return Response(order_items_deserialized)
