from django.shortcuts import render,HttpResponse

# Create your views here.

#定义视图函数

from app01.models import BookInfo,HeroInfo

def index(request):
    #进行处理，和M和T交互
    # return HttpResponse('okkkk')
    b = BookInfo.objects.filter(id=1)[0].btitle

    context = {'latest_question_list': b,'list':list(range(1,10))}
    return render(request,'booktest/index.html',context)

def index2(request):
    return HttpResponse('hello python')

def show_books(request):
    '''显示图书信息'''
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request,'booktest/show_books.html',context)

def detail(request,id):
    '''查询图书关联的英雄信息'''
    book = BookInfo.objects.get(id=id)
    heros = book.heroinfo_set.all()
    context = {'heros':heros,'book':book}
    return render(request,'booktest/detail.html',context)