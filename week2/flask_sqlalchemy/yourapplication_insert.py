# coding: utf-8
from yourapplication import User
users=User.query.all
users
users=User.query.all()
users
other=User('other','other@example.com')

from yourapplication import db
db.session.add(other)
db.session.commit()
users=User.query.all()
users
py = Category('Python')
Category

from yourapplication import Category,Post
py = Category('Python')
p = Post('Hello Python!','Python is pretty cool',py)
db.session.add(py)
db.session.add(p)
db.session.commit()
py.posts()
