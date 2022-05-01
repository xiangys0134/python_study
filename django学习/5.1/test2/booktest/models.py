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

    # @classmethod
    # def create_book(cls,btitle,bpub_date):
    #     # 1.创建一个图书类对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #
    #     # 2.保存进数据库
    #     obj.save()
    #
    #     # 3.返回obj
    #     return obj

    class Meta:
        db_table = 'bookinfo'


    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    isDelete = models.BooleanField(default=False)
    # 关系属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

#   新闻类型类
class NewsType(models.Model):
    type_name = models.CharField(max_length=20)
    type_news = models.ManyToManyField('NewsType')

class NewInfo(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #关联属性
    # news_type = models.ManyToManyField('NewsType')

# 员工基本信息类
class EmployeeBasicInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    age = models.IntegerField()

# 员工详细信息类
class EmployeeDetailInfo(models.Model):
    addr = models.CharField(max_length=256)
    # 教育经历

    # 关系属性，代表员工的基本信息
    emplyee_basic = models.OneToOneField('EmployeeBasicInfo',on_delete=models.CASCADE)

class AreaInfo(models.Model):
    '''地区模型类'''
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)


