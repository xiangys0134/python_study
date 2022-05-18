from django.db import models

# Create your models here.

class DomainInfo(models.Model):
    '''域名信息模型类'''
    dname = models.CharField(max_length=60,unique=True,blank=True)
    port = models.IntegerField(default=443)
    project = models.CharField(max_length=50,null=True)
    #标记删除
    # isDelete = models.BooleanField(default=False)
    # 标记是否部署
    isDeploy = models.BooleanField(default=True)

    # 关系属性
    dwhoiscompany = models.ForeignKey('Whoiscompany',on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'domaininfo'

    def __str__(self):
        return self.dname

class Whoiscompany(models.Model):
    '''基于whois认证'''
    name = models.CharField(max_length=20,unique=True,blank=True)
    # url = models.CharField(max_length=100)

    class Meta:
        db_table = 'whoiscompany'

    def __str__(self):
        return self.name










