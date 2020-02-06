from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField( max_length=32,verbose_name="书籍名称")
    pub_date=models.DateField(verbose_name="出版日期")
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="价格")
    publish=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE,null=True,verbose_name="出版社")
    authors=models.ManyToManyField("Author",db_table="book2authors") # 创建关系表
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="书籍"

class Publish(models.Model):
    name=models.CharField( max_length=32,verbose_name="名字")
    city=models.CharField( max_length=32)
    email=models.CharField(max_length=32)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="出版社"

class Author(models.Model):
    name=models.CharField( max_length=32)
    age=models.IntegerField()
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
