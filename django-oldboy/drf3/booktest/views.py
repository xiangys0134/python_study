from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
from booktest.models import BookInfo,HeroInfo
from rest_framework import views,viewsets
from booktest.serializers import BookInfoSeralizers,HeroInfoSerializer

class BookView(View):
    def get(self,request):
        books = BookInfo.objects.all()
        data = [
            {"id":1,"btitle":"红楼梦"},
            {"id":2,"btitle":"西游记"},
            {"id":3,"btitle":"三国演义"},
            {"id":4,"btitle":"水浒传"},
        ]
        data = []
        for book in books:
            data.append(
                {"id":book.id,"btitle":book.btitle}
            )
        return JsonResponse(data=data,safe=False)

class BookInfoView(viewsets.ModelViewSet):
    "视图类"
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSeralizers

######################
from rest_framework import views
from rest_framework.response import Response
class HeroInfoAPIView(views.APIView):
    def get(self,request):
        herros = HeroInfo.objects.all()
        # data = HeroInfoSerializer.validated_data
        Serializer = HeroInfoSerializer(instance=herros,many=True)
        # print(Serializer.is_valid())
        print(herros)
        print("data:>",Serializer)
        return Response(Serializer.data)
