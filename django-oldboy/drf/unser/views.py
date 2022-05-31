from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from unser.serializers import BookInfoSerializer

class BookInfoAPIView(APIView):
    def post(self,request):
        data = request.data
        # print(data)
        serializer = BookInfoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.validate
        print(result)
        return Response({"methods":"post"})