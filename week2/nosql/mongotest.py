# coding: utf-8
from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db = client.louplus

if __name__ == '__main__':
    user1 = {'user_id':1000,'name':'shiyan','pass':10,'study_time':50}
    user2 = {'user_id':2000,'name':'Lou','pass':15,'study_time':171}
    db.user.delete_many({'user_id':1000})
    db.user.delete_one({'user_id':2000})

    db.user.insert_one(user1)
    db.user.insert_one(user2)

#db.user.find_one({'name':'dian'})
#db.user.update_one({'name':'dian'},{'$set':{'age':7,'addr':['FI','CN']}})
#db.user.find()
#db.user.find_one({'name':'dian'})
    for user in db.user.find():
        print(user)
    
