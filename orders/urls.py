from django.urls import path
from orders.views import ListCreateOrderView, RetrieveUpdateDestroyOrderView

urlpatterns = [
    path("orders/", ListCreateOrderView.as_view()),
    path("orders/<int:order_id>", RetrieveUpdateDestroyOrderView.as_view()),
]
