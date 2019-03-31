# coding: utf-8
import redis
r = redis.StrictRedis(host='127.0.0.1',db=0)

if __name__ == '__main__':
    user1 = {'user_id':1000,'name':'shiyan','pass':10,'study_time':50}
    user2 = {'user_id':2000,'name':'Lou','pass':15,'study_time':171}
    
    r.hmset('user1',user1)
    r.hmset('user2',user2)
    r.hset('user3','name','dian')
    r.ping
    r.ping()
    r.hgetall('user')
