from django.db import models

# Create your models here.

class BookInfo(models.Model):
    '''图书管理类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'booktest_bookinfo'



