#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
author:yousong.xiang 2018.10.31
v1.0.3
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
1.去除空格
2.将'+ -' 转变为 '-' 号
3.获取空格最内层内容
4.换算  作为一个计算函数 可通过findall进行匹配获取第一个元素
5.替换    sear()获取第一值进行替换
'''

import re


def sub_indent(str1):
    str1 = re.sub('\s+','',str1)
    #将字符串进行替换，例如- - 替换成+
    str1 = str(str1).replace('--', '+')

    #将字符串进行替换-+ 替换成-，+- 替换成-
    str1 = str(str1).replace('-+','-')
    str1 = str(str1).replace('+-','-')
    str1 = str(str1).replace('++','+')

def sub_sesult(value,count=0):
    ''' 计算参数值，例如4*2998+10*568/14'''
    value = sub_indent(value)

    if re.findall('[-]?\d+[\.]?\d{0,}[\*\/\+\-]',value):
        if re.findall(r'[-]?\d+[.]?\d{0,}[*/][-]?\d+[.]?\d{0,}',value):
            ret = re.search(r'[-]?\d+[.]?\d{0,}([*/][-])?\d+[.]?\d{0,}',value)    #获取值4*2998

            b = re.findall(r'[-]?\d+[.]?\d{0,}([*/])[-]?\d+[.]?\d{0,}',value)[0]
            #分割符
            str_split = ''.join(b)
            num_first = str(ret).split(str_split)[0]
            num_second = str(ret).split(str_split)[1]

            if num_first.isdigit():
                num_first = int(num_first)
            else:
                num_first = float(num_first)

            if num_second.isdigit():
                num_second = int(num_second)
            else:
                num_second = float(num_second)

            # 运算获取结果
            if str_split == "+":
                count += (num_first + num_second)
            elif str_split == "-":
                count += (num_first - num_second)
            elif str_split == "*":
                count += (num_first * num_second)
            elif str_split == "/":
                count += (num_first / num_second)

            if count >= 0:
                count = r'+'+ str(count)
            #将匹配的值替换成对应的count





        #re.search(r'[-]?\d+[.]?\d{0,}[*/]?[+-]?[]')

