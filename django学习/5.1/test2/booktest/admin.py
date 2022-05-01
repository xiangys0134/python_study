from django.contrib import admin

# Register your models here.

from booktest.models import HeroInfo,BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle','bprice','bpub_date','bread','bcomment']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','hcomment']


admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(BookInfo,BookInfoAdmin)
