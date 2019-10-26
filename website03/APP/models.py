from django.db import models

# Create your models here.

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Users(models.Model):
    u_name = models.CharField(max_length=16)
    u_age = models.IntegerField(default=1)
    u_addr = models.CharField(max_length=16)




