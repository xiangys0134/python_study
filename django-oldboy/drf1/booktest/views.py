from django.shortcuts import render

from rest_framework import viewsets
# Create your views here.
from booktest.models import BookInfo,HeroInfo
from booktest.serializers import BookInfoSerializers,HeroInfoSerializers

class BookInfoAPIView(viewsets.ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializers

########################################
from rest_framework.views import APIView
from rest_framework import response

class HeroInfoAPIView(APIView):
    def get(self,request):
        herors = HeroInfo.objects.filter(id=3)
        # print(herors)
        # 调用序列化器，参数1就是要序列化的书写，就是模型查询出来的结果
        Serializer = HeroInfoSerializers(instance=herors,many=True)

        return response.Response(Serializer.data)