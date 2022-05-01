from django.db import models

# Create your models here.

#图书类
class BookInfo(models.Model):
    '''图书模型类'''
    #CharField说明是一个字符串，max_length指定字符串长度
    btitle = models.CharField(max_length=20)
    # 图书的出版日期，DateField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        #返回书名
        return self.btitle


class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    #性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)

    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.hname
