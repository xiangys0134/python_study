from django.db import models

# Create your models here.

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    pub_date = models.DateField()   #"2012-12-12"
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author",db_table="author2book")

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.title

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    class Meta:
        db_table = "publish"

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ad = models.OneToOneField("AuthorDetail",on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "author"

class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=32)




