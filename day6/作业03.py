#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
"""

import re

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def cal_str(str1,count=0):
    """
    计算字符串如16-3*2的值
    :param str1:
    :param count:
    :return:
    """
    str1 = str(str1)
    str1 = str(str1).replace('-+','-')
    str1 = str(str1).replace('+-','-')
    str1 = str(str1).replace('++','+')
    str1 = str(str1).replace('--','+')

    if re.search('^[\-]?\d+[\+\-\*\/]+',str1):
        if re.search('\d+[*/][-]?\d+',str1):
            # print('aaa')
            fist1 = re.search('\d+[\.]?\d{0,}[*/][-]?\d+[\.]?\d{0,}',str1)
            fist_new = fist1.group()
            # print(fist1)
            # print(fist_new)

            #取'*','/'符号
            str_split = re.findall('[*/]',fist_new)[0]
            # print(str_split)

            num_first = fist_new.split(str_split)[0]
            # print(num_first)

            num_second = fist_new.split(str_split)[1]
            # print(num_second)

            if num_first.isdigit():
                num_first = int(num_first)
            else:
                num_first = float(num_first)

            if num_second.isdigit():
                num_second = int(num_second)
            else:
                num_second = float(num_second)

            if str_split == "*":
                count += (num_first * num_second)
            else:
                count += (num_first / num_second)

            # print(count)

            str1 = re.sub('\d+[\.]?\d{0,}[*/][-]?\d+[\.]?\d{0,}',str(count),str1,1)
            print(str1)

        elif re.search('\d+[\.]?\d{0,}[+-[-]?\d+',str1):
            fist1 = re.search('[-]?\d+[\.]?\d{0,}[+-][-]?\d+[\.]?\d{0,}', str1).group()
            print(fist1)

            print(str1+'#####')
            # 取'*','/'符号
            str_split = re.findall('[+-]', fist1)[-1]
            print(str_split)

            # num_first = fist1.split(str_split)[1]
            # print(num_first)

            num_first = re.search('^[-]?\d+[\.]?\d{0,}',fist1).group()
            print(num_first)

            num_second = re.search('[+-]+\d+[\.]?\d{0,}$',fist1).group()
            print(num_second)

            if num_first.isdigit():
                num_first = int(num_first)
            else:
                num_first = float(num_first)

            print(num_first,type(num_first))

            if num_second.isdigit():
                num_second = int(num_second)
            else:
                num_second = float(num_second)

            print(num_second,type(num_second))

            count += num_first + num_second
            print(count)

            str1 = re.sub('[-]?\d+[\.]?\d{0,}[+-][-]?\d+[\.]?\d{0,}',str(count),str1,1)
            print(str1+'&&&&')
            print(count)

        # cal_str(str1,count)

        cal_str(str1,count)
    else:
        return count



a = cal_str('-9-24-7+8')

print(a)

def foo(str1):
    """
    字符串替换求值
    :param str1:
    :return:
    """
    str1 = str(str1).replace('-+','-')
    str1 = str(str1).replace('+-','-')
    str1 = str(str1).replace('++','+')
    str1 = str(str1).replace('--','+')

    str1 = str(str1).replace(' ','')
    # print(str1)

    if re.findall(r'^\-?\d+[\+\-\*\/]+',str1):
        # print('aaa')
        # first1 = re.findall('\([^()]+\)',str1)
        if re.findall('\([^()]+\)',str1):
            # print(first1)
            first1 = re.findall('\([^()]+\)',str1)[0].strip('()')
            # print('ccc',first1)


# foo(a)