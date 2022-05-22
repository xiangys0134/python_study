from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateTimeField()
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)

    class Meta:
        db_table = "book"

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)