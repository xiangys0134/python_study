from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01 import models

def books(request):
    queryset = models.Book.objects.all()
    print(queryset)

    for obj in queryset:
        print(obj.title)
    return render(request,"books.html",locals())

def addbooks(request):
    if request.method =="GET":
        return render(request,"addbooks.html")
    else:

        # book = models.Book(title="linux",price=100,pub_date="2012-10-12",publish="苹果出版社")
        # book.save()
        models.Book.objects.create(title=request.POST.get("title"),price=request.POST.get("price"),pub_date=request.POST.get("pub_date"),publish=request.POST.get("publish"))

    return redirect("/books/")


def delbook(request,id):
    models.Book.objects.filter(id=id).delete()
    return redirect("/books/")


def editbook(request,id):
    if request.method == "GET":
        return render(request,"editbook.html")
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        pub_date = request.POST.get("pub_date")
        models.Book.objects.filter(id=id).update(title=title,price=price,publish=publish,pub_date=pub_date)
        return redirect("/books/")

def add(request):
    # models.Publish.objects.create(name="老男孩出版社",addr="深圳")
    publish_obj = models.Publish.objects.filter(name="橘子出版社").first()
    models.Book.objects.create(title="java",price=100,booktype="计算机",pub_date="2012-05-11",publish=publish_obj)
    return HttpResponse("添加成功")

