from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from booktest.models import BookInfo,HeroInfo,AreaInfo
from datetime import date
def index(request):
    '''显示图书信息'''
    # 1.查询出所有图书的信息
    books = BookInfo.objects.all()

    context = {'books':books}
    # 2.使用模板
    return render(request,'booktest/index.html',context)

def create(reqeust):
    '''新增图书视图'''
    # 1.创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)

    # 2.保存
    b.save()

    return redirect('/index')

def delete(request,id):
    '''删除点击的图书'''
    # 1.通过id获取到对应图书对象
    book = BookInfo.objects.get(id=id)
    book.delete()
    return redirect('/index')


def areas(request):
    '''获取广州的上级地区和下级地区'''
    # 1.获取广州市的信息
    area = AreaInfo.objects.get(atitle='广州市')

    # 2.查询广州市的上级地区
    parent = area.aParent.atitle

    # 3.查询广州市的下级地区
    children = area.areainfo_set.all()

    context = {'area':area,'parent':parent,'children':children}
    return render(request,'booktest/areas.html',context)

