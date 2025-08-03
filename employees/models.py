from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)  # Added photo field

    def __str__(self):
        return self.name

# Create your models here.
