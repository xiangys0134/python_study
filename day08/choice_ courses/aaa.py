#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys,pickle

db_dir = os.path.dirname(os.path.abspath(__name__))
# db_dir = os.path.dirname(dir)
print(db_dir)

roles_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(roles_db_dir,'roles.db')):
    with open(os.path.join(roles_db_dir,'roles.db'),'rb') as f:
        f1 = f.read()
        roles = pickle.loads(f1)

# print(roles)

#读取用户账号密码表
userpass_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(userpass_db_dir,'userpass.db')):
    with open(os.path.join(userpass_db_dir,'userpass.db'),'rb') as f:
        f1 = f.read()
        userpass = pickle.loads(f1)

# print(userpass)

sutent_course_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(sutent_course_db_dir,'sutent_course.db')):
    with open(os.path.join(sutent_course_db_dir,'sutent_course.db'),'rb') as f:
        f1 = f.read()
        sutent_course = pickle.loads(f1)

# print(sutent_course)

select_course_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(select_course_db_dir,'select_course.db')):
    with open(os.path.join(select_course_db_dir,'select_course.db'),'rb') as f:
        f1 = f.read()
        select_course = pickle.loads(f1)

# print(select_course)

grade_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(grade_db_dir,'grade.db')):
    with open(os.path.join(grade_db_dir,'grade.db'),'rb') as f:
        f1 = f.read()
        grade = pickle.loads(f1)

grade_teacher_db_dir = os.path.join(db_dir,'db')
if os.path.exists(os.path.join(grade_teacher_db_dir,'grade_teacher.db')):
    with open(os.path.join(grade_teacher_db_dir,'grade_teacher.db'),'rb') as f:
        f1 = f.read()
        grade_teacher = pickle.loads(f1)
print(grade_teacher)