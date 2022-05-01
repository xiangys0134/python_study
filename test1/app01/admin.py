from django.contrib import admin
from app01.models import BookInfo,HeroInfo
# Register your models here.

# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    '''英雄模型类管理类'''
    list_display = ['id','hname','hgender','hcomment','hbook']
#注册模型类

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)