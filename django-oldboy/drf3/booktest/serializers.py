from rest_framework import serializers
from booktest.models import BookInfo

class BookInfoSeralizers(serializers.ModelSerializer):
    "图书管理序列化类"
    class Meta:
        model = BookInfo
        fields = "__all__"

class HeroInfoSerializer(serializers.Serializer):
    "声明式要转换的数据字段格式"
    id = serializers.IntegerField(label="主键ID")
    hname = serializers.CharField(label="姓名")
    hgender = serializers.IntegerField(label="性别")
    hcomment = serializers.CharField(label="技能描述")

