# -*- coding: utf-8 -*-
"""利用上下文实现间隔打印"""

class Indenter(object):
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print_(self, text):
        print '    ' * self.level + text

with Indenter() as indent:
    indent.print_('hi!')
    with indent:
        indent.print_('locke')
        with indent:
            indent.print_('cucumnber')
    indent.print_('over')