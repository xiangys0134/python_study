from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    #CharField说明是一个字符串
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=20)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname



