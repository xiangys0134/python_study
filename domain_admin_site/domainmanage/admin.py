from django.contrib import admin
from domainmanage.models import DomainInfo,Whoiscompany

# Register your models here.

class DomainInfoAdmin(admin.ModelAdmin):
    '''域名信息模型'''
    list_per_page = 10  #指定每页显示10条数据
    list_display = ['dname','port','isDeploy','project']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['dname','project']
    search_fields = ['dname','project']


class WhoiscompanyAdmin(admin.ModelAdmin):
    '''域名运营商模型'''
    list_per_page = 10  #指定每页显示10条数据
    list_display = ['name',]
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(DomainInfo,DomainInfoAdmin)
admin.site.register(Whoiscompany,WhoiscompanyAdmin)
