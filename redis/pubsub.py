# -*- coding: utf-8 -*-
'''
使用redis构造发布订阅模式
'''
import redis
import time

class Suber(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(db=5)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe('task:pubsub:channel')

    def listen_msg(self):
        for msg in self.ps.listen():
            time.sleep(1)
            if msg["type"] == 'message':
                print "get message:", msg['data']

if __name__ == '__main__':
    print 'listen task channel'
    suber = Suber()
    suber.listen_msg()
