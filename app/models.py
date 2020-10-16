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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", null=True)

    def __str__(self):
        return self.customer.name


class Provider(models.Model):
    name = models.CharField(max_length=200, null=True)


class Branch(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="bprovider", null=True)
    location = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    contactPerson = models.CharField(max_length=200, null=True)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="delivers", null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="dprovider", null=True)
    date = models.DateField(null=True)
    pickupDate = models.DateField(null=True)
    status = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)


class Voucher(models.Model):
    proofDocument = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    date = models.CharField(max_length=200)


class Designation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee", null=True)
    basicSal = models.CharField(max_length=200, null=False)
    role = models.CharField(max_length=200, null=True)


class Adjustments(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employeenum", null=True)
    type = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=False)
    date = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)



class Salary (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employeeno", null=True)
    month = models.CharField(max_length=200, null=True)
    addition = models.CharField(max_length=200, null=True)
    deduction = models.CharField(max_length=200, null=True)
    total = models.CharField(max_length=200, null=True)
    issueDate = models.DateField(null=False)



class Attendance (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employeeid", null=False)
    date = models.DateField(null=True)
    type = models.CharField(max_length=200, null=True)
    outTime = models.CharField(max_length=200, null=True)
    inTime = models.CharField(max_length=200, null=True)


class Department(models.Model):
    name = models.CharField(max_length=200, null=True)


class Documents(models.Model):
    name = models.CharField(max_length=200, null=True)
    docCode = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    docType = models.CharField(max_length=200, null=True)
    issueAuthority = models.CharField(max_length=200, null=True)
    createDate = models.DateField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="documents", null=True)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    reference_number = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="product", null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
