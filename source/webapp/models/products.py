from django.db import models
from webapp.models.base import BaseModel
from webapp.models.statuses import StatusChoices
from webapp.managers import ProductManager


class Product(BaseModel):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    image = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Image'
    )
    category = models.CharField(
        verbose_name='Category',
        choices=StatusChoices.choices,
        max_length=100,
        default=StatusChoices.OTHER
    )
    rest = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Rest'
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
        verbose_name='Price'
    )

    objects = ProductManager()

    def __str__(self):
        return f"{self.title} - {self.category} - {self.price}"

    class Meta:
        db_table = "product"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
