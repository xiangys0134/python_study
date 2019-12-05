from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app.models import Book

def index(request):
    ret = Book.objects.all()
    return render(request,"index.html",locals())

def addbooks(request):
    if request.method == "GET":
        return render(request,"addbooks.html")

    # print(request.POST.get("title"))
    Book.objects.create(title=request.POST.get("title"),price=request.POST.get("price"),publish=request.POST.get("publish"),pub_date=request.POST.get("pub_date"))
    return redirect("/index/")

def delbooks(request,id):
    # print(id)
    Book.objects.filter(id=id).delete()
    return redirect("/index/")

def updatebooks(request,id):
    if request.method=="GET":
        ret = Book.objects.filter(id=id)[0]
        print(id,ret.title)
        return render(request,"updatebooks.html",locals())
    title = request.POST.get("title")
    price = request.POST.get("price")
    publish = request.POST.get("publish")
    pub_date = request.POST.get("pub_date")
    Book.objects.filter(id=id).update(title=title,price=price,publish=publish,pub_date=pub_date)
    return redirect("/index/")









