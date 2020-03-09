from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01 import models

def books(request):
    quertset = models.Book.objects.all()


    return render(request,"books.html",locals())



def add(request):
    if request.method =="GET":
        publish_list = models.Publish.objects.all()
        author_list = models.Author.objects.all()
        return render(request,"addbook.html",locals())
    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        data.pop("authors_list")

        #绑定多对多
        #linux这本书绑定两个作者
        book = models.Book.objects.create(**data)

        #为用户绑定数据作者
        book_id = request.POST.getlist("authors_list")
        book.authors.add(*book_id)
    return redirect("/books/")


def delete(request,id):
    queryset = models.Book.objects.filter(id=id).first()
    ret = models.Book.objects.filter(id=id).delete()
    for i in queryset.authors.all():
        i.delete()
    return redirect("/books/")


def change(request,id):
    ret = models.Book.objects.filter(id=id).first()
    author_list = models.Author.objects.all()
    publish_list = models.Publish.objects.all()
    if request.method == "GET":
        return render(request,"change.html",locals())
    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        if request.POST.getlist("authors_list"):
            data.pop("authors_list")

        # print(data)

        #绑定多对多
        #linux这本书绑定两个作者
        book = models.Book.objects.filter(id=id).update(**data)
        book = models.Book.objects.filter(id=id).first()

        #为用户绑定数据作者
        book_id = request.POST.getlist("authors_list")
        # print(book_id,type(book_id))
        # print("book",book)
        # book.authors.clear()
        # book.authors.add(*book_id)
        return redirect("/books/")