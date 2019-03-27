#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqldb://root:990113@localhost:3306/shiyanlou_1'

db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>'% self.name

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('category',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=created_time
        self.category=category
        self.content=content

# def __repr__(self):
#        return '<File %r>' % self.title
