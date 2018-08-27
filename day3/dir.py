#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
#日志处理邮件发送
#yousong.xiang QQ:250919938 2018.8.23
#v1.0.0

import re,os,sys,time,socket,commands,smtplib

#import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header

##邮件发送
def msg_send(user,password,receivers,title,content):
    # 第三方 SMTP 服务
    mail_host = "smtp.qiye.163.com" # SMTP服务器
    #mail_user = "ops@xuncetech.com" # 用户名
    #mail_pass = ".FgX~/D?Lrhvun;" # 密码

    #sender = 'ops@xuncetech.com' # 发件人邮箱(最好写全, 不然会失败)
    sender = user # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['250919938@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #title = 'Python SMTP Mail Test' # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8') # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) # 启用SSL发信, 端口一般是465
        smtpObj.login(user, password) # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


#sourcdir = sys.argv[1]
##hostname_err变量为传递
#hostname_err = sys.argv[2]

#file_tmp变量用来存放报错信息
file_tmp = "/tmp/file_tmp.txt"
#变量tb1用来存储错误日志路径、行数
tb1 = {}

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


#获取本机电脑名
#myname = socket.getfqdn(socket.gethostname())
#获取本机ip
#myaddr = socket.gethostbyname(myname)


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


#各个子系统日志
def xc_logs():
    a = os.popen('find /data/www/*/storage/logs -type d')
    line = a.readlines()
    for i in line:
        print i
        os.system('python /data/script/logs_check.py %s'%(i.replace('\n','')))

#系统级别日志
def system_logs():
    msg1_dir = "/var/log"
    msg1_log = "syslog"
    os.system('python /data/script/logs_check.py %s %s'%(msg1_dir,msg1_log))

#获取本机计算机名
myname = commands.getstatusoutput('hostname')[1]
#获取本机IP地址
myaddr = get_host_ip()


#file1 = "/tmp/file_tmp.txt"
if os.path.exists(file_tmp):
    os.remove(file_tmp)


#收集应用系统日志
xc_logs()

#收集系统级别日志
system_logs()


f3 = open(file_tmp,"a+")
file_lines = f3.read()
f3.close()

if file_lines:
    msg_send('ops@xuncetech.com', '.FgX~/D?Lrhvun;',['xiao.li@xuncetech.com','yousong.xiang@xuncetech.com','shaobo.zheng@xuncetech.com','song.wu@xuncetech.com'],'日志:' + myaddr + myname,file_lines)
