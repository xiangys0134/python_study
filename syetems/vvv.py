#!/usr/bin/python
# -*- coding: utf-8 -*-
#检查错误日志行数,对目录进行检索，将可查看的日志进行分类处理
#yousong.xiang QQ:250919938 2018.8.16
#v1.0
#$1--------->日志路径basename
#$2--------->报错日志的主机标识
#$3--------->检查的日志名称,选填.目前没有对$3进行判断处理

import re,os,sys

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header

##邮件发送
##user,pwd,to,header_txt,content_txt
def msg_send(user,pwd,to,header_txt,content_txt,fulltxt):
    msg = MIMEMultipart()
    msg['Subject'] = Header(header_txt,'utf-8')
    msg['From'] = Header(user)

    content1 = MIMEText(content_txt,'plain', 'utf-8')
    msg.attach(content1)

    att = MIMEText(open(fulltxt, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=fulltxt)
    msg.attach(att)

    s = smtplib.SMTP('smtp.sina.com')
    s.set_debuglevel(1)
    s.starttls()
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()

sourcdir = sys.argv[1]
hostname_err = sys.argv[2]

#file1 = "D:\messages"
#file2 = "D:\messages_new"

def file_check(file1,file2,file3):
    ##打开源文件及目标文件
    if os.path.exists(file1):
        f1 = open(file1, "r")
    else:
        print "查询文件异常"
        exit(4)
    if os.path.exists(file2):
        os.remove(file2)
        f2 = open(file2, "a+")
    else:
        f2 = open(file2, "a+")

    count = 0
    for line in f1:
        if "centos1" in line.lower() or "dhcprequest" in line.lower() or "unknown" in line.lower():
            f2.write(line)
            count += 1

    f1.close()
    f2.close()
    #print count
    if count > 0:
        #print "存在报错日志...."
        count = "报错行数为:" + str(count)
        file3 += file1
        msg_send('xiangys_0134@sina.com', 'meiyoumima~!@0', ['250919938@qq.com','xiangys0134@sina.com'],file3 + "存在日志错误", count,file2)


if len(sys.argv) == 4:  #切换单个文件
    print "aaa"
    sourcfile = sys.argv[4]
    file1 =os.path.join(sourcdir,sourcfile)
    file2 = os.path.join('/tmp',sourcfile)
    file_check(file1,file2,hostname_err)
else:
    ##根据目录进行日志分类,切换日志
    files = os.listdir(sourcdir)
    for i in files:
        if re.search('\.log$',i):
             #print i
             file1 = os.path.join(sourcdir,i)
             file2 = os.path.join('/tmp',i)
             file_check(file1,file2,hostname_err)
