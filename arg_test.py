# -*- coding: utf-8 -*-
__author__ = 'LPP'

import sys
def readfile(filename):
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

if len(sys.argv) < 2:
    print 'no action specified'
    sys.exit()
if sys.argv[1].startswith('--'): #starts with
    option = sys.argv[1][2:]   #截取第二个参数中第三个及其以后的字符
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print 'help'

    else:
        print 'unknown option'
    sys.exit()
else:
    for filename in sys.argv[1]:
        readfile(filename)

'''在 cmd type python D:\appium\PyCharm\workplace\test\example1\arg_test.py --version
   output:Version 1.2
'''