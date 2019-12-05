from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    booktype=models.CharField(max_length=32,null=True)
    pub_date = models.DateField()

    publish=models.OneToOneField("Publish",on_delete=models.CASCADE,unique=None)
    # publish=models.ForeignKey("Publish",on_delete=models.CASCADE,unique=True)
    authors=models.ManyToManyField("Author",db_table="book2author")

    class Meta:
        db_table="book"


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

    class Meta:
        db_table="publish"


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


    class Meta:
        db_table="author"


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    gf = models.CharField(max_length=32)
    cid = models.CharField(max_length=32)
    author=models.OneToOneField("Author",on_delete=models.CASCADE)

    class Meta:
        db_table="authordetail"




