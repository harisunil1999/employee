from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    employee_id=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    possition=models.CharField(max_length=200)
    employee_status=models.CharField(max_length=200)
    gender=models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    
