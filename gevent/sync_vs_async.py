# -*- coding: utf-8 -*-
import gevent
import datetime

def task(gid):
    gevent.sleep(1)
    print 'task {} done'.format(gid)

def synchronous():
    for i in xrange(0, 5):
        task(i)

def asynchronous():
    jobs = [gevent.spawn(task, i) for i in xrange(0, 5)]
    gevent.joinall(jobs)

print 'begin sync'
sync_start = datetime.datetime.now()
synchronous()
print 'sync spend {}'.format(datetime.datetime.now() - sync_start)

print 'begin async'
async_start = datetime.datetime.now()
asynchronous()
print 'async spend {}'.format(datetime.datetime.now() - async_start)
