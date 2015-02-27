#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 15-2-6 by LPP

import re
s = '(abc)def'
m = re.search("(\(.*\)).*",s)
print m.group(1)

s1 = 'adkkdk'
s2 = 'abc123efg'
an = re.search('^[a-z]+$',s1)
if an:
    print "s1:",an.group(),'全为小写'
else:
    print s1,'全不是小写'
an = re.match('[a-z]+$',s2)
if an:
    print 's2:',an.group(),'全为小写'
else:
    print s2,'不全是小写'