from django.shortcuts import render,HttpResponse

from django.http import JsonResponse
from booktest.models import BookInfo


# Create your views here.
def get_books(request):
    data = []
    books = BookInfo.objects.all()
    for book in books:
        data.append({
            "id":book.id,
            "btitle":book.btitle
        })
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii':False})

from django.views import View

class BookInfoView(View):
    def get(self,request):
        return JsonResponse({"method":"get"})

    def post(self,request):
        return JsonResponse({"method":"post"})

    def put(self,request):
        return JsonResponse({"method":"update"})

    def delete(self,request):
        return JsonResponse({"method":"destory"})