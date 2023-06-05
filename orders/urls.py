from django.urls import path
from orders.views import ListOrderView

urlpatterns = [
    path("orders/", ListOrderView.as_view()),
]
