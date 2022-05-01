#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os,subprocess

# ret = os.popen("dir",
#                )

ret = subprocess.Popen("dir",
                 shell=True,
                 stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE

)
print(ret.stdout.read().decode("gbk"))