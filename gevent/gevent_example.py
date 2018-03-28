# -*- coding: utf-8 -*-
"""
gevent打了monkey patch之后会设置python相应的模块设置成非阻塞，
然后在内部实现epoll的机制，一旦某一个套接字调用非阻塞的IO(比如recv)都会理解返回，
并且设置一个回调函数，这个回调函数是用于切换到当前子coroutine，设置好回掉函数之后就把控制权返回给主coroutine，主coroutine继续调度。
一旦网络I/O准备就绪，epoll会触发之前设置的回调函数，从而引发主coroutine切换到子coroutine，做相应的操作。
"""

urls = ['http://lockecucumber.com', 'http://www.baidu.com', 'http://www.python.org']

import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

import urllib2

def print_head(url):
    print 'Starting %s' % url
    data = urllib2.urlopen(url).read()
    print '%s: %s bytes: %r' % (url, len(data), data[:50])

jobs = [gevent.spawn(print_head, url) for url in urls]

gevent.joinall(jobs)