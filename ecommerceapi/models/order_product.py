from django.db import models
from models.order import Order
from models.product import Product

class OrderProduct(models.Model):

    product = models.models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.models.ForeignKey(Order, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Order Product")
        verbose_name_plural = ("Order Productsesesesesssss")

    def __str__(self):
        return f'Order {self.order.id} contains {self.product}'
