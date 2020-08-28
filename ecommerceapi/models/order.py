from django.db import models
from .customer import Customer
from .payment_type import PaymentType


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment_type = models.ForeignKey(
        PaymentType, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")

    def __str__(self):
        return f'Order was created by {self.customer.first_name} {self.customer.last_name} at {self.created_at}.'
