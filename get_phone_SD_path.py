#!-*- coding:utf-8 -*-
__author__ = 'LPP'

import os
import subprocess
'''
print 'os.path=',os.path
print 'os.environ=',os.environ
rootDir = os.path.dirname(os.path.join(os.environ["ANDROID_HOME"], "build-tools"))
print 'rootDir=',rootDir
rootDir = rootDir+'\\a.txt'
#os.remove(rootDir)
'''
cmd1 = ["adb","shell"]
child1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
#print child1.stdout.read()

cmd2 = ["cd","sdcard"]
child2 = subprocess.Popen(cmd2, stdin=child1.stdout,stdout=subprocess.PIPE)

cmd3 = ["rm",".a8a3_1944_91d5_aa08_18b0"]
child3 = subprocess.Popen(cmd3, stdin=child2.stdout,stdout=subprocess.PIPE)






