# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


client = MongoClient()
db = client.shiyanlou
contests = db.contests
records = db.contests.find()
def get_rank(user_id):
    rank=0
    score=0
    submit_time=0
    users_list=[]
    users_set = set()
    for record in db.contests.find():
        dict_tmp={}
        id_tmp=record['user_id']
        rank=record['challenge_id']
        score=record['score']
        time=record['submit_time']

        if id_tmp in users_set:
            for item in users_list:
                if item['id']==id_tmp:
                    item['score']+=score
                    item['submit_time']+=time
                    break
            
        else:
            dict_tmp['id']=id_tmp
            dict_tmp['score']=score
            dict_tmp['submit_time']=time
            users_set.add(id_tmp)
            users_list.append(dict_tmp)

    newlist=sorted(users_list,key=lambda k:(-k['score'],k['submit_time']))
    rank, score, submit_time=0,0,0
    for index,item in enumerate(newlist):
        item['rank']=index+1    
        if item['id']==user_id:
            rank=item['rank']
            score=item['score']
            submit_time=item['submit_time']

    return rank, score, submit_time


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('please input user id')
        exit(1)
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        exit(2)

    if db.contests.find_one({'user_id':user_id})==None:
        print("NOTFOUND")
    else:
        userdata = get_rank(user_id)
        print(userdata)
