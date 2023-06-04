from django.urls import path
from menu.views import ListCreateMenuItemView, ListCreateCategoryView

urlpatterns = [
    path('menu-items', ListCreateMenuItemView.as_view()),
    path('categories', ListCreateCategoryView.as_view())
]
