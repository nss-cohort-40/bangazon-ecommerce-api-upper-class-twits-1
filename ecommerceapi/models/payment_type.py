from django.db import models
from .customer import Customer

# Create your models here.


class PaymentType(models.Model):
    merchant_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    expiration_date = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = ("payment type")
        verbose_name_plural = ("payment types")

    def __str__(self):
        return f'{self.merchant_name} {self.account_number}'
