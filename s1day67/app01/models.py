from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=128)

    def __str__(self):
        return self.order_id