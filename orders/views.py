from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from orders.serializers import OrderItemSerializer, OrderSerializer


# Create your views here.
class ListOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest):
        user = request.user

        if user.is_superuser or user.groups.filter(name="Manager").exists():
            orders = Order.objects.all()
            print("admin")
        elif user.groups.filter(name="Delivery Crew").exists():
            orders = Order.objects.filter(delivery_crew=user)
            print("delivery")
        else:
            orders = Order.objects.filter(user=user)
            print("customer")

        serialized_orders = OrderSerializer(orders, many=True)

        return Response(serialized_orders.data)
