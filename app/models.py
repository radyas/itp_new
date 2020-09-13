from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    nic = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name


class Order(models.Model):
    brand = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    shipAddress = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders",null=True)

    def __str__(self):
        return self.customer.name
