from django.db import models
from .order import Order
from .product import Product


class OrderProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("order product")
        verbose_name_plural = ("order products")

    def __str__(self):
        return f'Order {self.order.id} contains {self.product}'
