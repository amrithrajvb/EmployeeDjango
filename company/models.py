from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100,unique=True)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    experience=models.IntegerField()

    def __str__(self):
        return self.emp_name

class Order(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    options = (("ordered", "ordered"), ("delivered", "delivered"),
               ("in_transit", "in_transit"), ("cancelled", "cancelled"))
    status = models.CharField(max_length=100, choices=options, default="ordered")
    phone = models.CharField(max_length=20)
    expected_deliverydate = models.DateField(null=True)


