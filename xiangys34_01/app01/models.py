from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
    class Meta:
        db_table="book"

class Myapp_person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30,unique=True)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'myapp_person'

class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'manufacturer'

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    num = models.IntegerField(unique=True)
    mid = models.ForeignKey(Manufacturer,models.CASCADE)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'car'


class Num(models.Model):
    id = models.AutoField(primary_key=True)
    cum = models.OneToOneField(to_field=Car.num)
    phone = models.IntegerField(unique=True)