from django.shortcuts import render,HttpResponse,redirect
from booktest.models import BookInfo,HeroInfo,AreaInfo
from datetime import date
# Create your views here.

def index(request):
    '''显示图书信息'''
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    '''新增一本图书'''
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    b.save()
    return redirect('/index')

def delete(request,id):
    b = BookInfo.objects.get(id=id)
    print('b>>>',b)
    b.delete()
    return redirect('/index')

def areas(request):
    '''获取广州2的上下级地区'''
    area = AreaInfo.objects.get(atitle='广州')
    parent = area.aParent
    children = area.areainfo_set.all()
    return render(request,'booktest/areas.html',{'area':area,'parent':parent,'children':children})
