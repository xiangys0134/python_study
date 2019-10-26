#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
yousong.xiang 2018.11.8
v1.0.1
学生选课系统
roles = {'user':'student','user01':'teacher'}
userpass = {'user':'123','user01':'abc'}
course = {'counrse':['c++','python','shell']}
select_course = {'user':['python','java'],'user2':['c++','linux']}
grade = {'12班':['user']}
默认管理用户用户：user01/abc 学生用户：user/123
"""
#用户角色表
roles = {'user':'Student','user01':'Manager'}
#用户账号密码表
userpass = {'user':'123','user01':'abc'}
#课程表
sutent_course = {'counrse':['c++','python','shell']}
#选课表
select_course = {'user':['python','java'],'user01':['python','java']}


class Manager:
    """
    老师类，拥有create_course、create_users、see_course、find_students、students_counrse、quit函数
    """
    selects = [
                      ('创建课程', 'create_course'),
                      ('创建账号', 'create_users'),
                      ('查看所有课程', 'see_course'),
                      ('查看所有学生', 'find_students'),
                      ('查看所有学生选课情况', 'students_counrse'),
                      ('退出', 'quit')
                      ]

    def __init__(self,name):
        self.name = name

    def tmp_list(self):
        count = 1
        while count <= len(self.selects):
            print(count, self.selects[count - 1][0])
            count += 1
        self.count = count

    def create_course(self,course):
        """
        创建课程函数
        :param course:
        :return:
        """
        # print(sutent_course['counrse'],'#####')
        if course in sutent_course['counrse']:
            print('新增的课程已经存在')
        else:
            sutent_course['counrse'].append(course)
            print(sutent_course)
            print('课程%s创建成功'%(course))

    def create_users(self,username,password):
        """
        创建学生账号，参数：用户名，密码
        :param username:
        :param password:
        :return:
        """
        for user in userpass.items():
            if user == username:
                print('该用户名已经存在,无法再创建')
                return 0

        userpass['userpass'] = password
        print('创建了学生账号%s,密码为%s'%(username,password))

    def see_course(self):
        """
        查看所有课程函数
        :return:
        """
        print('课程名:',end='')
        for i in sutent_course['counrse']:
            print(i,end=' ')
        print('\n')
        # print('查看所有课程')

    def find_students(self):
        """
        查看所有学生函数
        :return:
        """
        print('学生：')
        for k,v in roles.items():
            if v == "Student":
                print(k,end='')
        # print('查看了所有学生')

    def students_counrse(self):
        """
        查看所有学生选课情况
        :return:
        """
        print(select_course)
        for k,v in roles.items():
            if v == "Student":
                print('学生：%s'%k)
                print('课程：',end='')
                # print(select_course[k])
                for i in select_course[k]:
                    print(i,end=' ')
                print('\n')


        # for k,v in select_course:
        #     print('学生：%s'%k)
        #     print('课程：',end='')
        #     for i in select_course[k]:
        #         print(i,end=',')
        # print('查看所有学生选select_course课情况')

    def quit(self):
        print('退出')
        exit()

class Student:
    """
    学生类
    """
    selects = [('查看所有课程', 'see_course'), ('所选课程', 'select_course'), ('退出', 'quit')]
    def __init__(self,name):
        self.name = name
        # self.course =

    def tmp_list(self):
        count = 1
        while count <= len(self.selects):
            print(count, self.selects[count - 1][0])
            count += 1

    def see_course(self):
        """
        查看所有课程函数
        :return:
        """

        print('课程名：',end='')
        for i in sutent_course['counrse']:
            print(i, end=' ')
        print('\n')
        # print('查看所有课程')

    def select_course(self):
        """
        查看所选函数
        :return:
        """
        print('学生：%s'%self.name)
        print('选课：',end='')
        # print(self.name)
        for i in select_course[self.name]:
            print(i,end=' ')
        print('\n')
        # print('所选课程：%s'%select_course[self.name])
        # print('所选课程')

    def quit(self):
        exit()
        print('退出')


insert_user = input('请输入用户名：').strip()
insert_pass = input('请输入密码：').strip()

# insert_user = 'user'
# insert_pass = '123'

for user,password in userpass.items():
    if user == insert_user and password == insert_pass:
        # print('登陆成功')
        if roles[insert_user] == "Student":
            # print(roles[insert_user],'###################')
            print('你的角色是[学生]，拥有学生权限')
            power_user = Student(insert_user)
        elif roles[insert_user] == "Manager":
            print('你的角色是[老师]，拥有管理员权限')
            power_user = Manager(insert_user)
        else:
            pass

        while True:
            # pass
            power_user.tmp_list()
            select_sub = input('请输入你的选项：')
            if select_sub.isdigit():
                try:
                    tmp = power_user.selects[int(select_sub)-1][1]
                    # print(tmp)
                    # print(tmp)

                    if hasattr(power_user,tmp):
                        ret = getattr(power_user,tmp)
                        # print(ret)
                        ss = ret.__code__.co_argcount
                        # print(ss)
                        if ss == 1:
                            ret()
                        elif ss > 1:
                            list_temp = []
                            for i in range(1,ss):
                                str1 = input('输入你想传入的参数：').strip()
                                list_temp.append(str1)
                            # print(list_temp)
                            ret(*list_temp)

                except Exception:
                    print('输入错误')
            else:
                print('请输入正确的数值')
else:
    print('登陆失败')








