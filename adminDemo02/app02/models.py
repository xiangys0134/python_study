from django.db import models

# Create your models here.
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

