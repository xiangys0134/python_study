from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField( max_length=32)
    pub_date=models.DateField()
    state=models.IntegerField(choices=((1,"已出版"),(2,"未出版")),default=1)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publish=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE,null=True)
    authors=models.ManyToManyField("Author",db_table="book2authors") # 创建关系表
    def __str__(self):
        return self.title

class Publish(models.Model):
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    gender=models.IntegerField(choices=((1,"男"),(2,"女")),default=1)
    #books=models.ManyToManyField("Book")
    ad=models.OneToOneField("AuthorDetail",null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class AuthorDetail(models.Model):
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)
    # author=models.OneToOneField("Author",on_delete=models.CASCADE)
    def __str__(self):
        return str(self.telephone)
'''
class book_authors(models.Model):
    book=models.ForeignKey("Book",on_delete=models.CASCADE)
    author=models.ForeignKey("Author",on_delete=models.CASCADE)

'''

class Emp(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    dep=models.CharField(max_length=32)
    province=models.CharField(max_length=32)

class Article(models.Model):
    title=models.CharField(max_length=32)
    comment_num=models.IntegerField()
    poll_num=models.IntegerField()
    def __str__(self):return self.title

class UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)