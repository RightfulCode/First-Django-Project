from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    cnic = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name 