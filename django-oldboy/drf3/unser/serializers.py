from rest_framework import serializers
from booktest.models import BookInfo,HeroInfo


def check_comment(data):
    # btitle = data.get("btitle")
    # bread = data.get("bread")
    if data > 10000:
        raise serializers.ValidationError('阅读量造假')
    else:
        return data

class BookInfoSeralizers(serializers.Serializer):
    "图书管理序列化类"

    id = serializers.IntegerField(label="ID",read_only=True)
    btitle = serializers.CharField(label="名称")
    bpub_date = serializers.DateField(label="发布日期")
    bread = serializers.IntegerField(label="阅读量",validators=[check_comment,])
    bcomment = serializers.IntegerField(label="评论量")
    is_delete = serializers.IntegerField(label="是否删除")

    # 验证单个字段
    # def validate_bread(self,data):
    #     if data < 0:
    #         # 错误信息
    #         raise serializers.ValidationError('阅读量不能为负数')
    #     else:
    #         # print('data',data)
    #         return data

    # 验证多个字段
    # def validate(self, attrs):
    #     btitle = attrs.get("btitle")
    #     bread = attrs.get("bread")
    #     if btitle !='西游记' or bread > 10000:
    #         raise serializers.ValidationError('读书标题重复，或者阅读量造假')
    #     else:
    #         return attrs

    # 第三种校验手段，在转换字段的限制选项中验证函数

    # 反序列化阶段
    def create(self,validated_data):
        instance = BookInfo.objects.create(
            btitle=validated_data.get("btitle"),
            # 对于日期字段还需要特殊处理
            bpub_date=validated_data.get("bpub_date"),
            bread=validated_data.get("bread"),
            bcomment=validated_data.get("bcomment"),
            is_delete=validated_data.get("is_delete")
        )
        return instance

    def update(self,instance,validated_data):
        instance.btitle = validated_data.get("btitle",instance.btitle)
        instance.bpub_date = validated_data.get("bpub_date",instance.bpub_date)
        instance.bread = validated_data.get("bread",instance.bread)
        instance.bcomment = validated_data.get("bcomment",instance.bcomment)
        instance.is_delete = validated_data.get("is_delete",instance.is_delete)
        instance.save()
        return instance

class HeroInfoSerializer(serializers.Serializer):
    "声明式要转换的数据字段格式"
    id = serializers.IntegerField(label="主键ID")
    hname = serializers.CharField(label="姓名")
    hgender = serializers.IntegerField(label="性别")
    hcomment = serializers.CharField(label="技能描述")

