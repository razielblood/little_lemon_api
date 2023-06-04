from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, related_name='delivery_crew', null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True, auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.user} - {self.date}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.order.id} - {self.menuitem} ({self.quantity})'

    class Meta:
        unique_together = ('order', 'menuitem')
