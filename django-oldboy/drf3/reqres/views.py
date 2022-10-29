from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# Create your views here.

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

class BookAPIView(APIView):
    def get(self,request):
        print(request)
        res = request.query_params.getlist("name")

        print(res)
        return Response({"message":"ok"})

    def post(self,request):
        print(request)
        res = request.data.getlist("btitle")

        print(res)
        return Response({"message":"ok"})

class BookView(APIView):
    def get(self,request):
        data = {
            "id":1,
            "btitle":"西游记",
            "bpubdate":"2016-10-16",
        }
        # 返回给客户端的http响应状态码

        return Response(data,status=status.HTTP_204_NO_CONTENT)