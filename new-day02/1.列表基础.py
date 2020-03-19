#!/usr/bin/env python
# -*- coding:utf-8 -*-


s = ["aa","bb","cc","dd"]

s2 = ["x","y","z"]
'''
总结：
1.列表的增有3种方法： append insert extend

s.append("xxy")
s.insert(2,"to2")

s.extend(s2)
print(s)

2.列表的删除有4种方法：pop remove clear del
pop：按位置删除
    p1 = s.pop()
    print(p1)
remove：按元素删除
    s.remove("bb")
    print(s)
    
clear：清空整个列表
    s.clear()
    print(s)  

del：删除某个元素，或者可以按照切片进行删除，或者可以删除整个列表
    del s[1]
    print(s)
    
    del s[:2:1]
    print(s)
    
    del s
    print(s)
    备注：这种方法del后字典就不存在了。所以你再打印的话就会报错

列表的修改： 
    1.按照索引修改
    s[:3] = "xxx bbb dddd"

    print(s)
    
    2.按照索引切片后修改值：其中值必须为可迭代对象(包括字符串和列表)
    s[:3] = [1,2,3]

    print(s)
    
    3.按照切片加步长则非常容器报错，因为切片和步长已经定义了值的数量
    
    
列表的查：
    1.按照索引，切片去查
    print(s[2])
    
    2.按照for循环去查
    
    for i in s:
        print(i)
    
其他方法：count len find index sort

find在python37中已经取消了，只能通过元素取找索引了
print(s.index("aa"))

sort重小到大排序，但是使用sort方法后会将原始的列表修改
l1 = [3,4,5,8,1,2,3]
l1.sort()
print(l1)


l1 = [3,4,5,8,1,2,3]
l1.reverse()

aList = [3,14,5,8,1,2,3]

aList.reverse()
print("List : ", aList)

'''

print(range(0,10))

# for i in range(10,0,-1):
#     print(i)

# aList = [3,14,5,8,1,2,3]
#
#
# for i in aList:
#     print(aList.index(i))

dic = {"a":123,"b":345}
dic.update(vv=789,a=234)

# print(dic)

# for key in dic.keys():
#     print(key)

# print(dic.values())

# for value in dic.values():
#     print(value)


for key,value in dic.items():
    print(key,value)












