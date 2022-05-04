from django.contrib import admin
from booktest.models import AreaInfo,PicTest
# Register your models here.

class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo

class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型'''
    list_per_page = 10 #指定每页显示10条数据
    list_display = ['id','atitle','parent','title']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle']    #列表右侧过滤栏
    search_fields =  ['atitle']

    fieldsets = (
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']})
    )

    inlines = [AreaStackedInline]
admin.site.register(AreaInfo,AreaInfoAdmin)
admin.site.register(PicTest)
