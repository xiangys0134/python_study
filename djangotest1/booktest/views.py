from django.shortcuts import render

from booktest.models import BookInfo,HeroInfo

from django.http import HttpResponse
from django.template import loader,RequestContext
# Create your views here.

def my_render(request,template_path,context_dir={}):
    temp = loader.get_template(template_path)

    context = RequestContext(request,context_dir)
    res = temp.render(context)
    return HttpResponse(res)

def index(request):
    # return my_render(request,'booktest/index.html',{})
    return render(request,'booktest/index.html',{'content':'hello world','list':list(range(1,10))})

def show_books(request):
    '''解释图书的信息'''
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',{'books':books})

def detail(request,bid):
    '''查询图书关联的英雄信息'''
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()

    return render(request,'booktest/detail.html',{'book':book,'heros':heros})
