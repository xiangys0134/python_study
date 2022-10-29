from django.shortcuts import render
from django.http import JsonResponse
from booktest.models import BookInfo,HeroInfo
from rest_framework import viewsets,views
from booktest.serializers import BookInfoSeralizers,HeroInfoSerializer

# Create your views here.

def get_books(request):
    books = BookInfo.objects.all()
    books_data = []
    for book in books:
        books_data.append({
            "id":book.id,
            "btitle":book.btitle
        })
    return JsonResponse(books_data,safe=False,json_dumps_params={'ensure_ascii': False})

from django import views
class BookInfoView(views.View):
    def get(self,request):
        heros = HeroInfo.objects.all()
        serializer = HeroInfoSerializer(instance=heros,many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        return JsonResponse({"methods":"post"})
    def put(self,request):
        return JsonResponse({"methods":"put"})
    def delete(self,request):
        return JsonResponse({"methods":"delete"})

    # def get(self,request):
    #     heros = HeroInfo.objects.all()
    #     serializer = HeroInfoSerializer(instance=heros,many=True)
    #     return JsonResponse(serializer.data,safe=False)