from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
import json
from book import models

def books(request):
    queryset = models.Book.objects.all()
    return render(request,"books.html",locals())


def addbook(request):
    if request.method=="GET":
        pub = models.Publish.objects.all().values()
        author = models.Author.objects.all()
        return render(request,"addbook.html",locals())

    #一对多 方式1
    title = request.POST.get("title")
    price = request.POST.get("price")
    publish = request.POST.get("publish")
    pub_date = request.POST.get("pub_date")
    author = request.POST.getlist("author")

    # publish_id = publish_obj.get("nid")
    print(title,price,publish,pub_date)
    # models.Book.objects.create(title=title,price=price,publish_id=1,pub_date=pub_date)


    #方式二
    publish_obj = models.Publish.objects.filter(name=publish).first()
    ret = models.Book.objects.create(title=title, price=price, publish=publish_obj,pub_date=pub_date)

    #查询go出版社的邮箱
    email = ret.publish.email
    # print(email)

    #多对多
    #绑定多对象的关系，无非是在关系表创建记录
    #一个作者绑定了两个作者
    user_list = []
    for i in author:
        author_id = models.Author.objects.filter(name=i).first()
        user_list.append(author_id)

    print(user_list)
    ret.authors.add(*user_list)
    return redirect("/books/")

def delbook(request,id):
    # user = models.Author.objects.all()
    #通过书籍id找user对象
    ret = models.Book.objects.filter(nid=id).first()
    models.Book.objects.filter(nid=id).delete()
    ret.authors.clear()
    return redirect("/books/")

def updatebook(request,id):
    if request.method == "GET":
        book = models.Book.objects.filter(nid=id).first()
        pub = models.Publish.objects.all()
        # authors = []
        # print(book.authors.all().first(),id,book)
        # for user in book.authors.all():
        #     if user:
        #         authors.append(user.name)
        # print(authors)

        authors = models.Author.objects.all()
        return render(request,"updatebooks.html",locals())
    title = request.POST.get("title")
    price = request.POST.get("price")
    pub_date = request.POST.get("pub_date")
    publish = request.POST.get("publish")
    authors = request.POST.getlist("author")
    publish_obj = models.Publish.objects.filter(name=publish).first()
    models.Book.objects.filter(nid=id).update(title=title,price=price,pub_date=pub_date,publish=publish_obj)
    ret = models.Book.objects.get(nid=id)
    authors_obj = []
    for user in authors:
        authors_query = models.Author.objects.filter(name=user).first()
        if authors_query:
            authors_obj.append(authors_query)
    print(authors_obj)
    ret.authors.clear()
    ret.authors.add(*authors_obj)
    return redirect("/books/")


def deletebook(request):
    response = {"code": 10000, "data": None, "msg": None}
    try:
        print(request.GET)
        id = request.GET.get("nid")
        ret = models.Book.objects.filter(nid=id).first()
        models.Book.objects.filter(nid=id).delete()
        ret.authors.clear()
        response["msg"]="ok"
        print(json.dumps(response))
    except Exception as e:
        response["code"] = 10001
        response["msg"] = e
    return HttpResponse(json.dumps(response))