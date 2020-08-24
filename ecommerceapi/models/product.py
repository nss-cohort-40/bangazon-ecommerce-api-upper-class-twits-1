from django.db import models
from .customer import Customer
from .product_type import ProductType

class Product(models.Model):

    title = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    price = models.DecimalField()
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=75)
    image_path = models.CharField(max_length=255)
    created_at = models.DateField()
    product_type_id = models.IntegerField(ProductType, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.title