from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from menu.models import Category, MenuItem
from menu.serializers import CategorySerializer, MenuItemSerializer
from menu.permissions import CategoryPermissions

# Create your views here.


class ListCreateCategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]


class ListCreateMenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
