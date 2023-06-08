from rest_framework import generics
from rest_framework.views import APIView
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Create your views here.
class ListAppendCartItemView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class RetrieveUpdateDestroyCartItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class DestroyCartView(APIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user__id=user.id)

    def delete(self, request):
        user = request.user
        Cart.objects.filter(user=user).delete()

        return Response({"message": "ok"}, status=status.HTTP_200_OK)
