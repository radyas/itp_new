from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    nic = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)


class Attendance(models.Model):
    in_time = models.DateTimeField(null=True),
    out_time = models.DateTimeField(null=True),
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)


class Salary(models.Model):
    month = models.DateField(null=True),
    issue_date = models.DateTimeField(null=True),
    total = models.FloatField(default=0.0),
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)


class Adjustment(models.Model):
    description = models.CharField(max_length=500, null=True),
    date = models.DateTimeField(null=True),
    amount = models.FloatField(default=0.0),
    type = models.CharField(max_length=50),
    employee_id = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
