from django.shortcuts import render,HttpResponse
from django.views import View
from django.http import JsonResponse
from booktest.models import BookInfo,HeroInfo
from rest_framework.viewsets import ModelViewSet
from booktest.serializers import BookInfoSerializer
# Create your views here.

class BookView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        books_data = []
        for book in books:
            books_data.append({
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date,
                "bread": book.bread,
                "bcomment": book.bcomment,
            })
        data = [
            {"id":1,"btitle":"红楼梦"},
            {"id":2,"btitle":"西游记"},
            {"id":3,"btitle":"水浒传"},
            {"id":4,"btitle":"三国演义"},
        ]
        return JsonResponse(data=books_data,safe=False,json_dumps_params={'ensure_ascii':False})

class BookInfoAPIView(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from booktest.serializers import HeroInfoSerializer

class HeroInfoAPIView(APIView):
    def get(self,request):
        heros = HeroInfo.objects.all()

        #调用序列化器
        # 参数1：要序列化的数据
        Serializer = HeroInfoSerializer(instance=heros,many=True)
        return Response(Serializer.data)

