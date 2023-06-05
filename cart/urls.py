from django.urls import path
from cart.views import ListAppendCartItemView, RetrieveUpdateDestroyCartItemView, DestroyCartView

urlpatterns = [
    path("cart/menu-items", ListAppendCartItemView.as_view()),
    path("cart/menu-items/", DestroyCartView.as_view()),
    path("cart/menu-items/<int:pk>", RetrieveUpdateDestroyCartItemView.as_view()),
]
