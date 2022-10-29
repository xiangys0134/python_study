from rest_framework import serializers
from booktest.models import BookInfo,HeroInfo

class BookInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        # fields = "__all__"
        fields = ("id","btitle")

class HeroInfoSerializers(serializers.Serializer):
    """英雄序列化类"""
    # 声明要转换的数据字段格式
    id = serializers.IntegerField(label="主键id")
    hname = serializers.CharField(label="姓名")
    hgender = serializers.IntegerField(label="性别")
    hcomment = serializers.CharField(label="描述信息")

