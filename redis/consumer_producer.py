# -*- coding: utf-8 -*-
'''
使用redis构造生产消费者模式
'''
import redis

class Consumer(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host="localhost", port=6379, db=5)
        self.queue = 'task:prodcons:queue'

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue, 10)
            if task:
                print 'Consumer get: ', task

if __name__ == '__main__':
    consumer = Consumer()
    consumer.listen_task()
