# -*- coding: utf-8 -*-


import subprocess

obj = subprocess.Popen(
    'dir',
    shell=True,
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE
)

err = obj.stderr.read()  # 标准错误输出
if err:
    print('出错啦！')
    print(err)
    # print(err.decode('gbk'))
else:
    ret = obj.stdout.read()  # 标准输出
    print(ret)
    # print(ret.decode('gbk'))

