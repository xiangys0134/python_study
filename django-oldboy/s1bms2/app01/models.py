from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    book_type = models.CharField(max_length=32,null=True)
    publish = models.CharField(max_length=32)
    pub_date = models.DateTimeField()
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author",db_table="book2author")

    class Meta:
        db_table = "book"

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

    class Meta:
        db_table = "publish"

class Author(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "author"

class AuthorDetail(models.Model):
    name = models.CharField(max_length=20)
    gf = models.CharField(max_length=32)
    uid = models.CharField(max_length=32,null=True)
    author = models.OneToOneField("Author",on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "authordetail"

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)