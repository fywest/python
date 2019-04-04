# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


client = MongoClient()
db = client.shiyanlou
contests = db.contests
records = db.contests.find()
records = {}
#if records is None:
#    return "NOTFOUND"

def get_rank(user_id):
    print(recodes)
    return recodes
    rank=0
    score=0
    submit_time=0
    users_list=[]
    users_set = set()
    for record in db.contests.find():
        dict_tmp={}
        list_tmp=[]
        id_tmp=record['user_id']
        rank=record['challenge_id']
        score=record['score']
        time=record['submit_time']
        dict_tmp[id_tmp]=list_temp

        if id_temp in users_set:
            for key,value in list_tmp:
                if key=id_tmp:
                    value[0]+=rank
                    value[1]+=score
                    value[2]+=time
            
        else:
            id_tmp=record['user_id']
            list_tmp.append(id_tmp)
            rank=record['challenge_id']
            list_tmp.append(rank)
            score=record['score']
            list_tmp.append(score)
            time=record['submit_time']
            list_tmp.append(time)
            dict_tmp[id_tmp]=list_temp
            users_set.add(id_tmp)
            user_list.append(dict_tmp)

    return user_list#rank, score, submit_time


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
