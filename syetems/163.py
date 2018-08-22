#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

def sendmail(user,password,receivers,title,content):
    # 第三方 SMTP 服务
    mail_host = "smtp.qiye.163.com"  # SMTP服务器
    #mail_user = "ops@xuncetech.com"  # 用户名
    #mail_pass = ".FgX~/D?Lrhvun;"  # 密码

    #sender = 'ops@xuncetech.com'  # 发件人邮箱(最好写全, 不然会失败)
    sender = user  # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['250919938@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #content = '过期教程害死人!'
    #title = 'Python SMTP Mail Test'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(user, password)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

sendmail('ops@xuncetech.com', '.FgX~/D?Lrhvun;', ['xiangys0134@sina.com', '250919938@qq.com'], '主题测试','CPU负载：1111')