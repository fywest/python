# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


client = MongoClient()
db = client.shiyanlou
contests = db.contests
records = db.contests.find()
#if records is None:
#    return "NOTFOUND"

def get_rank(user_id):
    rank=0
    score=0
    submit_time=0
    users_list=[]
    users_set = set()
    for record in db.contests.find():
        print(record)
        dict_tmp={}
        list_tmp=[]
        id_tmp=record['user_id']
        rank=record['challenge_id']
        score=record['score']
        time=record['submit_time']

        if id_tmp in users_set:
            print('---------------')
            for item in users_list:
                if item['id']==id_tmp:
                    print(item)
                    item['value'][1]+=rank
                    item['value'][2]+=score
                    item['value'][3]+=time
                    print(item)
                    break
            
        else:
            print('*********')
            list_tmp.append(id_tmp)
            list_tmp.append(rank)
            list_tmp.append(score)
            list_tmp.append(time)
            dict_tmp['id']=id_tmp
            dict_tmp['value']=list_tmp
            print(dict_tmp)
            users_set.add(id_tmp)
            users_list.append(dict_tmp)
        print(users_set)


    return users_list#rank, score, submit_time


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('please input user id')
        exit(1)
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        exit(2)
    userdata = get_rank(user_id)
    print(userdata)
