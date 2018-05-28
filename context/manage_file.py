# -*- coding: utf-8 -*-
"""自己实现一个处理文本的上下文处理器， 我们用来写个文件"""

class ManageFile(object):

    def __init__(self, file_name, handle):
        self.file_name = file_name
        self.handle = handle
    
    def __enter__(self):
        self.file = open(self.file_name, self.handle)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManageFile('hello.txt', 'w') as f:
    f.write('haha')