#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from booktest.models import BookInfo,HeroInfo

class BookInfoSerializer(serializers.ModelSerializer):
    '''图书序列化器'''
    class Meta:
        model = BookInfo
        fields = "__all__"

class HeroInfoSerializer(serializers.Serializer):
    '''手动书写字段'''
    id = serializers.IntegerField(label="主键ID")
    hname = serializers.CharField(label="姓名")
    hgender = serializers.IntegerField(label="性别")
    hcomment = serializers.CharField(label="技能描述")
