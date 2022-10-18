from django.db import models
from webapp.models import BaseModel


class Order(BaseModel):
    product = models.ManyToManyField(
        to='webapp.Product',
        related_name='orders',
        verbose_name='Products',
        through='webapp.ProductOrder',
        through_fields=['order', 'product']
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Name'
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Phone'
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Address'
    )

    def __str__(self):
        return f"{self.phone}  {self.name}"

    class Meta:
        db_table = "orders"
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
