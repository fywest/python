# coding: utf-8
from myapplication import File,Category,db
File.query.all()
Category.query.all()
db.session.query(File).all()
db.session.query(File.id).all()
db.session.query(File.id,File.title,File.category_id).all()
db.session.query(File.id,File.title,File.category_id).filter(File.id=1).all()
db.session.query(File.id,File.title,File.category_id).filter(File.id==1).all()
db.session.query(File.id,File.title,File.category_id,Category.id).filter(File.id==1).all()
db.session.query(File.id,File.title,File.category_id,Category.id).filter(File.id==1).filter(File.category_id==Category.id).all()
db.session.query(File.id,File.title,File.category_id,Category.name).filter(File.id==1).filter(File.category_id==Category.id).all()
db.session.query(File.id,File.content,Category.name).filter(File.id==1).filter(File.category_id==Category.id).all()
db.session.query(File.id,File.content,Category.name).filter(File.id==1).filter(File.category_id==Category.id).all()
