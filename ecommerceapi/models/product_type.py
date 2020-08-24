from django.db import models


class ProductType(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("Product Type")
        verbose_name_plural = ("Product Typesesesesesesessss")

    def __str__(self):
        return self.name
