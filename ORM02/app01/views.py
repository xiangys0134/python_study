from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from app01.models import Book

def add(request):
    # 添加操作2
    book = Book.objects.create(title="go",price=100,publish="橘子出版社",pub_date="2003-05-06")
    book = Book.objects.create(title="java",price=300,publish="香蕉出版社",pub_date="2007-05-06")
    print(book.title)
    print(book.publish)
    return HttpResponse("添加成功")


def query(request):

    # 1 all()：查询所有记录
    # book = Book.objects.all()
    # for i in book:
    #     print("i",i.title)
    # print("book",book)
    # print("count:",book.count())

    # 2 first() last() #查询第一个切片数据和最后一个切片数据
    # book_obj = Book.objects.all().first()
    # print(book_obj.title)

    # 3 filter()    #条件匹配查询
    # book_obj = Book.objects.all().filter(id=1).first()
    # print(book_obj.title)

    # 4 get()    #条件匹配查询
    # query = Book.objects.get(title="python")
    # print(query.title)

    # 5排查方法
    # query = Book.objects.exclude(title="python")
    # for i in query:
    #     print(i.title)
    # # print(query.title)

    # 6排序
    # query = Book.objects.all().order_by("-price")
    # for i in query:
    #     print(i.title,i.price)

    # 7反向排序
    # query = Book.objects.all().order_by("-price").reverse()
    # for i in query:
    #     print(i.title,i.price)

    # 7 exists
    # ret = Book.objects.filter(title="ruby").exists()
    # if ret:
    #     print("ok")
    # else:
    #     print("not exists")

    # ret = Book.objects.all().filter(price=100).values_list("title","price")
    # for i in ret:
    #     print(i[0],i[1])

    # 8 去重
    # ret = Book.objects.values("price").distinct()
    # print(ret)

    # 查询价格大于100的数据
    # ret = Book.objects.filter(price__gte=100)
    # print(ret.values("title"))

    #查询书籍名称以py开头
    # ret = Book.objects.filter(title__startswith="Li").values("title")
    # print(ret)

    #查询包含ava的字符
    ret = Book.objects.filter(title__contains="ava").values("title")
    print(ret)
    return HttpResponse("查询成功")