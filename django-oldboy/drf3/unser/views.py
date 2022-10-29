from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from unser.serializers import HeroInfoSerializer,BookInfoSeralizers
from booktest.models import BookInfo,HeroInfo
# Create your views here.

class BookInfoAPIView(APIView):
    def get(self,request):
        print(request.data)
        books = BookInfo.objects.all()
        seralizers = BookInfoSeralizers(instance=books,many=True)
        return Response(seralizers.data)
    def post(self,request):
        # print(request.data)
        serializer = BookInfoSeralizers(data=request.data)
        # 交易客户端提交的数据是否正常
        ret = serializer.is_valid(raise_exception=True)
        if ret:
            serializer.save()
        # print('ret',ret)
        # result = serializer.validated_data
        # print('validated_data:>>',result)

        return Response({"methods":"post"})

    def put(self,request,pk):
        book = BookInfo.objects.get(id=pk)
        putserializer = BookInfoSeralizers(instance=book,data=request.data,partial=True)
        ret = putserializer.is_valid(raise_exception=True)
        print('ret:>>>>',ret)
        if ret:
            putserializer.save()

        return Response({"methods": "put"})