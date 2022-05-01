from django.db import models


# Create your models here.

class AreaInfo(models.Model):
    '''地址模板类'''
    atitle = models.CharField(verbose_name='标题',max_length=20)
    aParent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest')