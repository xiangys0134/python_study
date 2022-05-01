from django.contrib import admin
from booktest.models import AreaInfo,PicTest

# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型管理类'''
    list_per_page = 2
    list_display = ['id','atitle','title']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle']
    search_fields = ['atitle']
    fields = ['aParent','atitle']
admin.site.register(AreaInfo,AreaInfoAdmin)

admin.site.register(PicTest)