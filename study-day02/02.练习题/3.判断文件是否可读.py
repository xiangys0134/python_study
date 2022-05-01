#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys



def main():
    sys.argv.append("")
    filename =  sys.argv[1]
    if not os.path.exists(filename):
        raise SystemExit(filename,+' does not exists')
    elif os.access(filename,os.R_OK):
        raise SystemExit(filename,+' is not accessible')
    else:
        print(filename,+' is accessiable')

if __name__ == '__main__':
    main()

