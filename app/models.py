from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    nic = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
