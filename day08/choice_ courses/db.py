#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
预先生成数据库文件
"""
import pickle,sys,os

dir = os.path.dirname(os.path.abspath(__name__))
dir = os.path.join(dir,'db')
print(dir)



#用户角色表
roles = {'user':'Student','user01':'Manager','test':'Teacher'}
#用户账号密码表
userpass = {'user':'123','user01':'abc','test':'123'}
#课程表
sutent_course = {'counrse':['c++','python','shell']}
#选课表
select_course = {'user':['python','java'],'user01':['python','java']}
#班级
grade = {'12班':['user']}
#讲师
grade_teacher = {'12班':'test'}


str_roles = pickle.dumps(roles)
print(str_roles)  #一串二进制内容
str_userpass = pickle.dumps(userpass)
str_sutent_course = pickle.dumps(sutent_course)
str_select_course = pickle.dumps(select_course)
str_grade = pickle.dumps(grade)
str_grade_teacher = pickle.dumps(grade_teacher)

if __name__ == '__main__':
    #生成roles表
    with open(os.path.join(dir,'roles.db'),'wb') as f:
        f.write(str_roles)

    with open(os.path.join(dir, 'userpass.db'), 'wb') as f:
        f.write(str_userpass)

    with open(os.path.join(dir, 'sutent_course.db'), 'wb') as f:
        f.write(str_sutent_course)

    with open(os.path.join(dir, 'select_course.db'), 'wb') as f:
        f.write(str_select_course)

    with open(os.path.join(dir, 'grade.db'), 'wb') as f:
        f.write(str_grade)

    with open(os.path.join(dir, 'grade_teacher.db'), 'wb') as f:
        f.write(str_grade_teacher)