# coding: utf-8
import redis
r = redis.StrictRedis(host='127.0.0.1',db=0)
r.ping
r.ping()
get_ipython().run_line_magic('save', 'redis_1.py 1:5')
r.hgetall('user')
get_ipython().run_line_magic('save', 'redis_1.py 1:6')
