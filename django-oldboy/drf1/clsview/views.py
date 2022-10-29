from django.shortcuts import render
from django.http import JsonResponse
from booktest.models import BookInfo
from rest_framework import views
# Create your views here.

def get_books(request):
    books_data = []
    books = BookInfo.objects.all()
    for book in books:
        books_data.append({
            "id":book.id,
            "btitle":book.btitle
        })
    return JsonResponse(books_data,safe=False)


class BookInfoView(views.View):
    def get(self,request):
        return JsonResponse({"methods":"get"})

    def post(self,request):
        return JsonResponse({"methods":"post"})

    def put(self,request):
        return JsonResponse({"methods":"put"})

    def delete(self,request):
        return JsonResponse({"methods":"delete"})

    def get2(self,request):
        return JsonResponse({"methods":"get2"})
