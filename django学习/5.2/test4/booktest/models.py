from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    '''图书模型管理类'''
    # 1.改变查询的结构集
    def all(self):
        # 1.调用父类的all方法获取所有数据
        books = super().all()

        # 2.对数据进行过滤
        books = books.filter(isDelete=False)

        return books

    # 2.封装函数：操作模型类对应的数据表
    def create_book(self,btitle,bpub_date):
        # 1.创建一个图书对象
        # book = BookInfo()
        # 获取self所在的模型类
        model_class = self.model
        book = model_class()
        book.btitle = btitle
        book.bpub_date = bpub_date

        book.save()
        return book

class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bprice = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    # bpub_date = models.DateField()
    # bpub_date = models.DateField(auto_now_add=True)
    bpub_date = models.DateField(auto_now=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0,null=True)
    #删除标记，软删除
    isDelete = models.BooleanField(default=False)

    #自定义一个BookInfoManager对象
    objects = BookInfoManager()

    class Meta:
        db_table = 'bookinfo'


    def __str__(self):
        return self.btitle
