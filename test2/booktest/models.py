from django.db import models

# Create your models here.

class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    hcomment = models.CharField(max_length=20,null=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname

class NewsType(models.Model):
    '''新闻'''
    type_name = models.CharField(max_length=20)

class NewsInfo(models.Model):
    '''新闻信息'''
    title = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    news_type = models.ManyToManyField('NewsType')

class EmployeeBasicInfo(models.Model):
    '''员工信息类'''
    name = models.CharField(max_length=20)
    gender = models.BooleanField(False)
    age = models.IntegerField()

class EmplyeeDatailInfo(models.Model):
    '''员工详细信息类'''
    addr = models.CharField(max_length=256)
    employee_baseci = models.OneToOneField('EmployeeBasicInfo',on_delete=models.CASCADE)

class AreaInfo(models.Model):
    '''地区模型类'''
    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
