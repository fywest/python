# -*- coding=utf-8 -*-

__author__ = 'Lauri'
__date__ = '2019.05.20'

'''
description: save json data to Redis
'''

import json
import redis

class RedisTT(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = '6379'
        self.r = redis.StrictRedis(host=self.host, port=self.port)

    def insertRedis(self,keyName,jsonStr):
        self.r.lpush(keyName, jsonStr)

def save1():
    someexpert = {}
    someexpert['id'] = 10000
    someexpert['realname'] = 'expert-a'
    someexpert['organization'] = 'BUAA'
    if RedisTT().r.exists('someexpert'):
        RedisTT().r.delete('someexpert')
    RedisTT().insertRedis(keyName='someexpert', jsonStr=json.dumps(someexpert))

def save2():
    frameworks = ['vue','react','angular']
    if RedisTT().r.exists('frameworks'):
        RedisTT().r.delete('frameworks')
    RedisTT().insertRedis(keyName='frameworks', jsonStr=json.dumps(frameworks))

if __name__ == "__main__":
    save1()
    save2()

    print(RedisTT().r.lrange('someexpert', 0, RedisTT().r.llen('someexpert')))
    print(RedisTT().r.lrange('frameworks', 0, RedisTT().r.llen('frameworks')))

