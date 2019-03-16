#!/usr/bin/en python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template

app=Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]= True

@app.route('/')
def index():
    teacher = {
        'name':'Aiden',
        'email':'luojin@simplecloud.cn'
    }
    
    course = {
        'name':'Pyhton Basic',
        'teacher':teacher,
        'user_count':5348,
        'price':199.0,
        'lab':None,
        'is_private':False,
        'is_member_course':True,
        'tags':['python','bigdata','Linux']
    }

    return render_template('index.html',course=course)

