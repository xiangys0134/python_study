from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from booktest.models import BookInfo
from generic.serializers import BookInfoSeralizers
from rest_framework.response import Response

class BookInfoAPIView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        obj = BookInfoSeralizers(instance=books,many=True)
        return Response(obj.data)

from rest_framework.generics import GenericAPIView

class BookInfo2APIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSeralizers
    def get(self,request):
        # books = BookInfo.objects.all()
        # obj = BookInfoSeralizers(instance=self.queryset,many=True)
        books = self.queryset
        obj = self.get_serializer(books)
        return Response(obj.data)

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
class BookInfo3APIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSeralizers
    def get(self,request):
        # books = BookInfo.objects.all()
        # obj = BookInfoSeralizers(instance=self.queryset,many=True)
        books = self.queryset
        obj = self.get_serializer(books)
        return Response(obj.data)