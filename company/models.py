from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100,unique=True)
    department=models.CharField(max_length=100)
    salary=models.IntegerField()
    experience=models.IntegerField()

    def __str__(self):
        return self.emp_name
