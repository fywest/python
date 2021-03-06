# coding: utf-8
get_ipython().run_line_magic('load', 'week2_flask_mysql_4.py')
# %load week2_flask_mysql_4.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:990113@localhost/shiyanlou_flask'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqldb://root:990113@localhost:3306/shiyanlou_flask?charset=utf8'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    def __init__(self, username,email):
        self.username=username
        self.email=email
    def __repr__(self):
        return '<User %r>'% self.username


   
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()
admin=User('admin','admin@example.com')
guest=User('guest','guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
users=User.query.all()
users
py = Category('Python')
p=Post('hello python','python is cool',py)
db.session.add(py)
db.session.add(p)
db.session.commit()
py.posts
py.posts.all()
