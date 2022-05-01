#!/user/bin/env python3
# -*- coding: utf-8 -*-

import getpass

user = getpass.getuser()
password = getpass.getpass('your password:')

print(user,password)