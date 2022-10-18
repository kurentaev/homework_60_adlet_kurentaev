from django.db import models


class ProductOrder(models.Model):
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    order = models.ForeignKey(
        to='webapp.Order',
        related_name='orders',
        on_delete=models.CASCADE,
        verbose_name='Order'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity'
    )

    def __str__(self):
        return f'{self.order} - {self.quantity}'

    class Meta:
        db_table = "product_order"
        verbose_name = 'Product and order '
        verbose_name_plural = 'Product and orders'
