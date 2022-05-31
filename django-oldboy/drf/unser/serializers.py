#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers
class BookInfoSerializer(serializers.Serializer):
    # 声明要转换的字段
    id = serializers.IntegerField(label='ID',read_only=True)
    btitle = serializers.CharField(label='名称',max_length=20)
    bpub_date = serializers.DateField(label='发布日期',required=False)
    bcomment = serializers.IntegerField(label='评论量',required=False)