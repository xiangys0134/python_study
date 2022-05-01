#!/user/bin/env python3
# -*- coding: utf-8 -*-

import fileinput


'''
fileinput有个好的地方就是可以导入文件也可以读取出来
'''

for line in fileinput.input():
    print(line,end='')

