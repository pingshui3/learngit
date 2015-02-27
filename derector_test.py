#! - *-coding:utf-8 -*-
__author__ = 'Liupp'
import os

def father(fn):
    print 'a,b,c'
    print fn.__name__
    return fn()

@father
def son1():
    tuple1 = [1,2,3]
    tuple2 = [2,3,4]
    u = zip(tuple1,tuple2)
    print u

pwd = 'D:\\appium\PyCharm\workplace\\test\example1\\arg_test.py'
print os.path.dirname(pwd)  #转到上级目录
