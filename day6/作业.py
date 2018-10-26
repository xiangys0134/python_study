#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
author:yousong.xiang 2018.10.27
v1.0.1
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
处理逻辑：
1.将字符串进行匹配最内层值，即不包含()符号的值
2.将值取出后计算出字符串的位置及括号内的值
3.计算括号内的值并通过字符串切片将字符串进行拼接
4.递归调用函数直到字符串中不在包含有()，则将最后的结果返回

做不出来了，在9-2*5/3+7/3*99/4*2998+10*568/14 在此类没有括号的时候的计算方式，先乘除后加减

'''
import re

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

#去除最里层的值
brackets='\([^\(\)]+\)'
# #加法正则匹配
# opp_add = r'(\d+\.?\d?+\d+\.?\d?)|(-\d+\.?\d?+\d+\.?\d?)'
# #减法正则匹配
# opp_sub = r'(\d+\.?\d?-d+\.?\d?)|(-\d+\.?\d?-\d+\.?\d?)'
# #乘法正则匹配
# opp_multi = r'(\d+\.?\d?*d+\.?\d?)|(-\d+\.?\d?*d+\.?\d?)'
# #除法正则匹配
# opp_div = r'(\d+\.?\d?/d+\.?\d?)|(-\d+\.?\d?/d+\.?\d?)'


#算术运算
def int_sub(value):
    '''获取值并进行计算'''
    #如果最后的值为-40之类则直接返回value
    ret = re.compile('[\+\-]')
    ret = ret.findall(value)
    ret = ''.join(ret)
    if ret == '+' or ret == '-':
        return value

    ##获取到+ - * /
    #value = -40/5
    ret = re.compile('[\-]?\d+[\.]?\d{0,}([\*\/\+\-]+)[\-]?\d+[\.]?\d{0,}')
    b = ret.findall(value)
    # b = re.findall('[\+\-\*\/]', value)



    str_split = ''.join(b)
    num_first = str(value).split(str_split)[0]
    print('47行测试:',num_first)
    num_second = str(value).split(str_split)[1]
    print('78行测试:',num_second)

    if num_first.isdigit():
        num_first = int(num_first)
    else:
        num_first = float(num_first)

    if num_second.isdigit():
        num_second = int(num_second)
    else:
        num_second = float(num_second)

    #运算获取结果
    if str_split == "+":
        count = num_first  + num_second
    elif str_split == "-":
        count = num_first - num_second
    elif str_split == "*":
        count = num_first * num_second
    elif str_split == "/":
        count = num_first / num_second
    return count


def foo(str1,count=0):
    #去除空格
    str1 = re.sub('\s+','',str1)
    #将字符串进行替换，例如- - 替换成+
    str1 = str(str1).replace('--', '+')

    #将字符串进行替换-+ 替换成-，+- 替换成-
    str1 = str(str1).replace('-+','-')
    str1 = str(str1).replace('+-','-')

    #获取最内层是否有匹配，如无匹配则返回[]，即return结果
    ret = re.compile(brackets)
    tmp = ret.findall(str1)
    print(tmp)
    if tmp:
        str_length_first = re.search(brackets,str1).span()[0]    #取值后的字符串位置：18
        str_length_second = re.search(brackets,str1).span()[1]    #取值后的字符串位置：25
        str_value = re.search(brackets,str1).group().strip('[()]')  #或者相关值：12.4 + 23
        print(str_value)
        # str_value = re.sub('\s+','',str_value)
        # # 将字符串进行替换，例如- - 替换成+
        # str1 = str(str1).replace('--', '+')
        sub_count = int_sub(str_value)

        #字符串拼接
        # print('长度&&&&',str_length_first)
        # print('长度&&&&',str_length_second)
        str_expr = str1[:str_length_first]+str(sub_count)+str1[str_length_second:]
        print('打印测试：',str_expr)
        return foo(str_expr,sub_count)
    else:
        if re.search('[\+\-\*\/]',str1):
            #此种类型方式9-2*5/3+7/3*99/4*2998+10*568/14
            first_ret = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).span(0)
            second_ret = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).span(1)
            count_str1 = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).group().strip('[()]')
            print('计算######',count_str1)
            sub_count = int_sub(count_str1)

            try:
                # 字符串拼接
                str_expr = str1[:first_ret] + str(sub_count) + str1[second_ret:]
                print('打印第二次测试:',str_expr)
                return foo(str_expr,sub_count)
            except Exception:
                return sub_count





test = foo(a)
print(test)

