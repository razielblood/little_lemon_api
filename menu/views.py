from rest_framework import generics
from menu.models import Category, MenuItem
from rest_framework.filters import SearchFilter, OrderingFilter
from menu.serializers import CategorySerializer, MenuItemSerializer
from menu.permissions import CategoryPermissions, MenuItemPermissions
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

# Create your views here.


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class RetrieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class ListCreateMenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields=['price',]
    search_fields=['category__title',]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class RetrieveUpdateDestroyMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermissions]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
