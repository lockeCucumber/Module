# -*- coding: utf-8 -*-
import gevent
import random

def task(gid):
    gevent.sleep(random.randint(0, 2))
    print 'task {} done'.format(gid)

def synchronous():
    for i in xrange(0, 5):
        task(i)

def asynchronous():
    jobs = [gevent.spawn(task, i) for i in xrange(0, 5)]
    gevent.joinall(jobs)

print 'begin sync'
synchronous()
print 'begin async'
asynchronous()
