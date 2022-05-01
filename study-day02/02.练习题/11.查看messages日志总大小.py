#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os

syslogs = [ log for log in os.listdir('/var/log') if log.startswith('messages')]

sum_size = sum([ os.path.getsize(os.path.join('/var/log',item)) for item in syslogs ])

print(sum_size)

