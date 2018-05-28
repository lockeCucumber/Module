# -*- coding: utf-8 -*-
"""通过contextlib实现一个上下文处理器"""

from contextlib import contextmanager

@contextmanager
def manage_file(file_name, handle):
    try:
        f = open(file_name, handle)
        yield f
    finally:
        f.close()

with manage_file('hello2.txt', 'w') as f:
    f.write('hello2')
