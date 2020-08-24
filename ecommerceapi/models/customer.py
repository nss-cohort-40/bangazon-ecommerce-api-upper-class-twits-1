from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)


class Meta:
    ordering = (F('user.date_joined').asc(nulls_last=True),)
