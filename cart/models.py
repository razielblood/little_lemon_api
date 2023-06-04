from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.user} - {self.menuitem} ({self.quantity})'

    class Meta:
        unique_together = ('user', 'menuitem')
