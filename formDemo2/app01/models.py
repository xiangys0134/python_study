from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=8,decimal_places=2)