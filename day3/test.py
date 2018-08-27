#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

t = int(time.strftime("%H%M%S"))
if 92450 >= t >= 92021:
    print(t)
else:
    print('eee')