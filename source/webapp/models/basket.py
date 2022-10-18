from django.db import models


class Basket(models.Model):
    product = models.ForeignKey(
        to='webapp.Product',
        related_name='products_order',
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Quantity',
        default=0,
    )

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

    def get_sum(self):
        return self.quantity * self.product.price

    @classmethod
    def get_total(cls):
        total = 0
        for basket in cls.objects.all():
            total += basket.get_sum()
        return total

    class Meta:
        db_table = "basket"
        verbose_name = 'Product order'
        verbose_name_plural = 'Product orders'
