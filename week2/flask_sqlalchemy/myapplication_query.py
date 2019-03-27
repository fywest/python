# coding: utf-8
from myapplication import db,File,Category
file=File.query.all()
file
file[0].title
file[0].created_time
file[0].category_id
file[0].content
category = Category.query.all()
category
