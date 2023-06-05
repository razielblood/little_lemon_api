from rest_framework import generics
from menu.models import Category, MenuItem
from menu.serializers import CategorySerializer, MenuItemSerializer
from menu.permissions import CategoryPermissions, MenuItemPermissions

# Create your views here.


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]


class RetrieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]


class ListCreateMenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermissions]


class RetrieveUpdateDestroyMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermissions]
