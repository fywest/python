# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    records = {}
    if records is None:
        return "NOTFOUND"
    rank=0
    score=0
    submit_time=0
    rank_list=[]
    users_set = set()
    for record in db.contests.find():
        rank_dict={}
        if record['user_id'] in users_set:
        rank += record['challenge_id']
        score += record['score']
        submit_time += record['submit_time']
        print("rank:{} score:{} submit_time:{}".format(rank,score,submit_time))
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
    userdata = get_rank(user_id)
    print(userdata)
