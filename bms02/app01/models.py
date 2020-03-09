from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author",db_table="book2author")

    class Meta:
        db_table="book"


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    ad = models.OneToOneField("AuthorDetail",null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr=models.CharField( max_length=64)
    # author = models.OneToOneField("Author",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.telephone)


class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)


class Article(models.Model):
    title = models.CharField(max_length=32)
    coment_num = models.IntegerField()
    poll_num = models.IntegerField()

