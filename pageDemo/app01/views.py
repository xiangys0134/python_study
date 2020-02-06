from django.shortcuts import render,redirect,HttpResponse

from app01.page import Pagination
from app01.models import Book
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import random
# Create your views here.


book_list= []
def index(request):
    '''
    for i in range(1,101):
        book = Book(title="book_%s"%i,price=random.randint(1,999))
        book_list.append(book)
    Book.objects.bulk_create(book_list)
    '''

    # book_list = Book.objects.all()

    # Paginator()

    #构建分页对象对象
    # paginator = Paginator(book_list,10)
    #
    # #分页器对象的功能
    # print(paginator.num_pages)  #分页数
    # print(paginator.count)  #100
    #
    # #展示页
    # page = paginator.get_page(1)
    # print(page.object_list) #第一页的关联数据

    '''
    book_list = Book.objects.all()
    paginator = Paginator(book_list,2)

    print(paginator.num_pages)  #分页数
    print(paginator.count)  #总条数100条
    print(">>>>",paginator.page_range)  #页码数range

    #单页对象(展示页)
    # page = paginator.get_page(paginator.num_pages)
    # page = paginator.get_page(2)
    # print(page.object_list) #获取该页第的数据
    #
    # print("page>>>>:",page)

    current_page = int(request.GET.get("page",1))



    #如果页数十分多时，换另一种显示方式
    if paginator.num_pages >11:
        if current_page-5 <0:
            page_range=range(1,12)

        elif current_page+5>paginator.num_pages:
            page_range=range(paginator.num_pages-10,paginator.num_pages+1)
        else:
            page_range = range(current_page-5,current_page+6)

    else:
        page_range = paginator.page_range

    page = paginator.get_page(current_page)

    last_page = paginator.num_pages
    get_list = paginator.object_list
    '''
    #自定义分页器##############
    from django.http.request import QueryDict
    print(request.GET)
    print(type(request.GET))

    book_list = Book.objects.all()
    current_page=request.GET.get("page")
    pagination=Pagination(current_page,book_list.count(),request,per_page=3)
    book_list=book_list[pagination.start:pagination.end]

    #保存搜索条件

    return render(request,"index2.html",locals())
