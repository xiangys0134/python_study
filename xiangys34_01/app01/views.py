from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import datetime
from django.urls import reverse
from app01.models import *
def index(request):
    hi = " Give me the strength to make my love fruitful in service."
    l1 = [11,22,33]
    now = datetime.datetime.now()
    L1 = ['alex', '金老板', '武佩琪']
    return render(request,'index.html',{"hi":hi,"l1":l1,"now":now,"L1":L1})


def order(request,month,year):
    return render(request,'order.html',locals())


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        user =  request.POST['user']
        pwd = request.POST['pwd']
        if user == 'alex' and pwd == '123':
            _url = reverse("index")
            # return redirect('/app01/index/')
            return redirect(_url)
        else:
            return render(request, 'login.html')


def add(request):
    #添加记录
    # book=Book(title='python',price="200",publish="人民出版社",pub_date="2012-12-12")
    # book.save()
    # book = Book.objects.create(title='go',price="150",publish="香蕉出版社",pub_date="2013-06-13")
    # print(book.title)
    # print(book.price)

    # manufacturer = Manufacturer.objects.create(name='小红')
    # print(manufacturer)
    car = Car.objects.create(mid_id=2,cname='宝马')
    print(car)
    return HttpResponse("添加成功")

def query(request):
    # 1.all()       查询所有记录
    # ret = Book.objects.all()
    # print(ret)
    # for obj in ret:
    #     print(obj.title)
    #     print(obj.price)
    # return HttpResponse("查询成功")

    # 2.first last  查询
    # book = Book.objects.all().filter(title='c++',price="100")
    # print(book[0].title)
    # if book:
    #     for obj in book:
    #         print(obj.title)
    # return HttpResponse('查询成功')

    # 5.get     get必须是有且只有一个匹配条件，要慎用
    # book=Book.objects.get(title='python')
    # print(book.title)
    # return HttpResponse('查询成功')

    # 5.排除方法
    # book = Book.objects.exclude(price=200)
    # if book:
    #     for obj in book:
    #         print(obj.title)
    # return HttpResponse('查询成功')

    #6.order_by
    # book=Book.objects.all().order_by("-price")
    # if book:
    #     for obj in book:
    #         print(obj.title)
    # return HttpResponse('查询成功')

    #reverse()
    # book=Book.objects.all().order_by("-price").reverse()
    # if book:
    #     for obj in book:
    #         print(obj.title)
    # return HttpResponse('查询成功')

    # 8.exists
    # book=Book.objects.all()
    # if Book.objects.all().exists():
    #     print("ok")
    # print(book)
    # return HttpResponse('查询成功')

    # book = Book.objects.all().exists()
    # if book:
    #     print("ok")
    # return HttpResponse('查询成功')

    #values计算
    # book = Book.objects.filter(price=100).values("title")
    #
    # print(book)
    # print(book.count())
    # for obj in book:
    #     print(obj['title'])
    # return HttpResponse('查询成功')

    #values
    # book = Book.objects.all().values("title").distinct()
    # print(book)
    # return HttpResponse('查询成功')


    #查询价格大于100的书籍
    # book = Book.objects.filter(price__gt=100)
    # if book:
    #     for obj in book:
    #         print(obj.title)
    # return HttpResponse('查询成功')

    #查询py开头的书籍
    book = Book.objects.filter(title__startswith='py')
    if book:
        for obj in book:
            print(obj.title)
    return HttpResponse('查询成功')




