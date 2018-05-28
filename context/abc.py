# -*- coding: utf-8 -*-
"""什么是上下文，看下下面的例子先"""

f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

with open('hello.txt', 'w') as f:
    f.write('hello, world!')

