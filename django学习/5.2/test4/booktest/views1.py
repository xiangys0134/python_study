from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from booktest.models import BookInfo

def index(request):
    context = {}
    return render(request,'booktest/index.html',context)

def index2(request):
    '''模板文件加载顺序'''
    return render(request,'booktest/index2.html')

# /temp_var
def temp_var(request):
    '''模板变量'''
    book = BookInfo.objects.get(id=1)
    context = {}
    context['my_dict'] = {'title':'字典键值'}
    context['my_list'] = [1,2,3]
    context['book'] = book

    return render(request,'booktest/temp_var.html',context)

# /temp_tags
def temp_tags(request):
    '''模板标签'''
    books = BookInfo.objects.all()
    context = {}
    context['books'] = books
    return render(request,'booktest/temp_tags.html',context)

def temp_filter(request):
    '''模板过滤器'''
    books = BookInfo.objects.all()
    context = {}
    context['books'] = books
    return render(request, 'booktest/temp_filter.html', context)

def temp_inherit(request):
    '''模板继承'''
    return render(request,'booktest/child.html')