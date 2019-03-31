# coding: utf-8
from pymongo import MongoClient
client=MongoClient('127.0.0.1',27017)
db = client.shiyanlou
for user in db.user.find():
    print(user)
    
user = {'name':'dian','age':7,'addr':['FIn','CN']}
db.user.insert_one(user)
db.user.find_one({'name':'dian'})
db.user.update_one({'name':'dian'},{'$set':{'age':7,'addr':['FI','CN']}})
db.user.update_one({'name':'dian'},{'$set':{'email':'dian@simplecloud.cn'}})
db.user.find()
db.user.find_one({'name':'dian'})
