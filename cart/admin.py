from django.contrib import admin
from menu.models import Category, MenuItem
from cart.models import Cart
from orders.models import Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)