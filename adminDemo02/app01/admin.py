from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
# Register your models here.

from . models import Book
from . models import Publish
from . models import AuthorDetail
from . models import Author

class PublishConfig(ModelAdmin):
    list_display = ["name","city","email"]


class BookConfig(ModelAdmin):
    def del_action(self,obj):
        return mark_safe("<a href="">删除</a>")

    def show_author(self,obj):
        print(obj.authors.all())
        authors = obj.authors.all()
        return " ".join([ obj.name for obj in authors ])

    list_display = ["title", "pub_date", "price","publish","del_action","show_author"]
    list_display_links = ["title","price"]
    list_filter = ["publish"]
    search_fields = ["title"]
    # list_editable = ["title"]
    # change_list_template = "mylist.html"

    def patch_init(self,request,queyset):
        queyset.updsate(price = 100)




admin.site.register(Book,BookConfig)
admin.site.register(Publish,PublishConfig)
admin.site.register(Author)
admin.site.register(AuthorDetail)

