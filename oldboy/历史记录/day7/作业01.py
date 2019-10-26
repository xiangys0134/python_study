#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:yousong.xiang 2018.10.31
#v1.0.1
#学生选课系统

'''
1.对象学生，可以查看所有课程，选择课程
2.对象管理员，创建账号，创建课程，查看课程，查看所有学生，查看所有学生选课
'''

#用户表
student = [{'username':'user01','password':'123','role':'student'},{'username':'user02','password':'123','role':'student'}]

#课程表
course = ['java','python','c++']

#选课表
select_course = [{'user':'user01','course':['java','python']}]

select_course1 = {
    'user1':{

    }

}

with open('roles','r',encoding='utf8') as f1:
    