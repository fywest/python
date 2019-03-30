import os
import json
from flask import Flask, render_template, abort
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

class Files(object):
    directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"files")
    def __init__(self):
        self._files = self._read_all_files()
    def _read_all_files(self):
        result = {}
        for filename in os.listdir(Files.directory):
            file_path=os.path.join(Files.directory,filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result
    def get_title_list(self):
        return [item['title'] for item in self._files.values()]
    def get_by_filename(self,filename):
        return self._files.get(filename)

files = Files()

class Files_mysql(object):
    def __init__(self):
        self._files=File.query.all()

    def __repr__(self):
        return self._files

    def get_title_list(self):
        title_list=[item.title for item in self._files]
        return title_list

    def get_file_list(self):
        file_list=[item for item in self._files]
        return file_list

    def get_id_list(self):
        id_list=[item.id for item in self._files]
        return id_list

    def get_file_by_id(self,fileid):
        file_dict={}
        for item in self._files:
            print(fileid,item.id)
            print(type(fileid),type(item.id))
            if int(fileid)==item.id:
                print(item)
                return item

    def get_file_category_by_fileid(self,fileid):
        file_query_test=db.session.query(File.id,File.content,File.created_time,Category.name).filter(File.id==fileid).filter(File.category_id==Category.id).first()
        print(file_query_test)
        return file_query_test
        
files_mysql=Files_mysql()

@app.route('/')
def index():
    return render_template('index.html',file_list=files_mysql.get_file_list())


#mysql> select file.id, file.content, file.created_time, catetory.name from file, category where file.id=1 and category.id=file.category_id
#db.session.query(File.id,File.content,Category.name).filter(File.id==1).filter(File.category_id==Category.id).all()
    
@app.route('/files/<fileid>')
def file(fileid):
    id_list=files_mysql.get_id_list()
    if int(fileid) not in id_list:
        abort(404)
    file_item_1=files_mysql.get_file_by_id(fileid)
    file_category_item=files_mysql.get_file_category_by_fileid(fileid)

    print(file_item_1)
    print(file_category_item)
    return render_template('file.html',file_item=file_category_item)

#@app.route('/files/<filename>')
#def file(filename):
#file_item=files.get_by_filename(filename)
#   if not file_item:
#       abort(404)
#    return render_template('file.html',file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    #app.run()

    files_mysql=Files_mysql()
    print(files_mysql.get_title_list())

    print(files_mysql.get_id_list())
    print(files_mysql.get_file_by_id(1))
    file_item=files_mysql.get_file_by_id(1)
    print(file_item.title)
    print(file_item.created_time)
    print(file_item.content)
    
    
    category_mysql = Category.query.all()
    print(category_mysql)

    file_query_test=db.session.query(File.id,File.content,Category.name).filter(File.id==1).filter(File.category_id==Category.id).all()
    print(file_query_test)
    

