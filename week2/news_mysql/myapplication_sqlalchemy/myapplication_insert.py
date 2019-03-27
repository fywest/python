# coding: utf-8

from myapplication import db
db.create_all()

from myapplication import Category,File

java = Category('Java')
python = Category('Python')

from datetime import datetime

file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
