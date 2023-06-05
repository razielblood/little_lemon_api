from rest_framework import generics
from rest_framework.views import APIView
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ListAppendCartItemView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyCartItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class DestroyCartView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        Cart.objects.filter(user=user).delete()

        return Response({"message": "ok"}, status=status.HTTP_200_OK)
