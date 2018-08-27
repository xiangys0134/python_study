#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
#检查错误日志行数,对目录进行检索，将可查看的日志进行分类处理
#yousong.xiang QQ:250919938 2018.8.25
#v1.0.3
#1.发送日志信息时不循环空文件
#2.解决新生产日志无法删除问题
#$1--------->日志路径basename
#$2--------->报错日志的主机标识
#$3--------->检查的日志名称,如果是只切换某个特定的日志则加上日志名称
#


import re,os,sys,time,socket,commands,smtplib

sourcdir = sys.argv[1]

#file_tmp变量用来存放报错信息
file_tmp = "/tmp/file_tmp.txt"
#变量tb1用来存储错误日志路径、行数
tb1 = {}

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])



def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

#获取本机计算机名
myname = commands.getstatusoutput('hostname')[1]
#获取本机IP地址
myaddr = get_host_ip()



##文件扫描函数,功能:检测error错误日志写入到字典中
def file_check(file1,file2):
    ##打开源文件及目标文件
    if os.path.exists(file1):
        f1 = open(file1, "r")
    else:
        print "查询文件异常"
        print file1
        return 9
    if os.path.exists(file2):
        os.remove(file2)
        f2 = open(file2, "a+")
    else:
        f2 = open(file2, "a+")

    count = 0
    for line in f1:
        if "error" in line.lower() or "exception" in line.lower():
            f2.write(line)
            count += 1

    f1.close()
    f2.close()
    #print count
    if count > 0:
        print "存在报错日志...."
        count = "报错行数为:" + str(count)
        #file3 += file1
        #os.remove(file2)
        tb1[file1] = count
    os.remove(file2)


#如果参的参数为$1=目录路径 $2=文件名称 则进行拼接处理,如果只传入$1 则循环$1目录下的文件进行拼接
if len(sys.argv) == 3: #切换单个文件
    #sourcfile变量主要用来切割系统日志 在脚本调用出写入具体的日志文件
    sourcfile = sys.argv[2]
    ##file1、file2分别为原始文件,目标错误文件 file2可以作为附件发送,但格式不标准
    file1 = os.path.join(sourcdir,sourcfile)
    file2 = os.path.join('/tmp',sourcfile)
    #file_check(file1,file2,hostname_err)
    file_check(file1,file2)
else:
    ##根据目录进行日志分类,切换日志
    files = os.listdir(sourcdir)
    for i in files:
        if re.search('\.log$',i):
             #print i
             file1 = os.path.join(sourcdir,i)
             file2 = os.path.join('/tmp',i)
             #file_check(file1,file2,hostname_err)
             file_check(file1,file2)
             time.sleep(1)

#将字典中的错误信息写入到一个文件中,读取文件内容后进行邮件发送

if tb1:
    f3 = open(file_tmp,"a+")
    f3.write('\n-----------------------------------------------start-----------------------------------------------------------\n')
    for k,y in tb1.items():
        f3.write("%s \t \t %s\n"%(k,y))

    f3.write('\n------------------------------------------------end------------------------------------------------------------\n')
    f3.write('\n\n\n\n')

    f3.close()


#print "aaaaaaaaaaaaaa"
#if os.path.exists(file2):
# os.remove(file2)
