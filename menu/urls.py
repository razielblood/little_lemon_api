from django.urls import path
from menu.views import (
    ListCreateMenuItemView,
    RetrieveUpdateDestroyMenuItemView,
    RetrieveUpdateDestroyCategoryView,
    ListCreateCategoryView,
)

urlpatterns = [
    path("menu-items", ListCreateMenuItemView.as_view()),
    path("menu-items/<int:pk>", RetrieveUpdateDestroyMenuItemView.as_view()),
    path("categories", ListCreateCategoryView.as_view()),
    path("categories/<int:pk>", RetrieveUpdateDestroyCategoryView.as_view()),
]
