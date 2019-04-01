from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


app = Flask(__name__)

app.config.update(dict(SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:990113@localhost:3306/shiyanlou_2',SQLALCHEMY_TRACK_MODIFICATIONS=True))

db = SQLAlchemy(app)

client=MongoClient('127.0.0.1',27017)
mongo_db=client.shiyanlou

class File(db.Model):
    __tablename__= 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category',uselist=False)
    content = db.Column(db.Text)
    

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def add_tag(self, tag_name):
        tag=mongo_db.user.find_one({'fileid':self.id})
        tag_name_list=tag['tag_name']
        print(tag_name_list)
        print(tag_name)
        if tag_name not in tag_name_list:
            tag_name_list.append(tag_name)
        print(tag_name_list)
        mongo_db.user.update_one({'fileid':self.id},{'$set':{'tag_name':tag_name_list}})

    def remove_tag(self, tag_name):
        tag=mongo_db.user.find_one({'fileid':self.id})
        tag_name_list=tag['tag_name']
        print(tag_name_list)
        print(tag_name)
        if tag_name  in tag_name_list:
            tag_name_list.remove(tag_name)
        print(tag_name_list)
        mongo_db.user.update_one({'fileid':self.id},{'$set':{'tag_name':tag_name_list}})


    @property
    def tags(self):
        tag=[]
        tag=mongo_db.user.find_one({'fileid':self.id})
        return ' '.join(tag['tag_name'])



class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self,name):
        self.name = name

def create_db():
    db.create_all()

def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

def insert_mongo_datas():
    file1_tag={'fileid':1,'tag_name':['tech','java','linux']}
    file2_tag={'fileid':2,'tag_name':['tech','python']}
    mongo_db.user.insert_one(file1_tag)
    mongo_db.user.insert_one(file2_tag)

def get_mongo_datas():
    for user in mongo_db.user.find():
        print(user)


@app.route('/')
def index():
    return render_template('index.html', files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html', file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
# app.run()
#create_db()
#insert_datas()    
    file1=File.query.first()
    print(file1)
    print(file1.id)
    print(file1.title)
    print(file1.tags)
    print(file1.add_tag('cooking'))
    print(file1.tags)
    print(file1.remove_tag('cooking'))
    print(file1.tags)
