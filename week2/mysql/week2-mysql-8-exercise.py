# coding: utf-8
get_ipython().run_line_magic('load', 'week2-mysql-8.py')
# %load week2-mysql-8.py
from sqlalchemy import create_engine

engine = create_engine('mysql://root:990113@localhost/shiyanlou',echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column (String(50))
    def __repr__(self):
        return "<User(name=%s)>" % self.name
        
print(User.__table__)
    
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('user.id'))
    teacher = relationship('User')
    def __repr__(self):
        return '<Course(name=%s)>'% self.name
        
print(Course.__table__)

class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='labs')
    def __repr__(self):
        return '<Lab(name=%s>'% self.name
 
print(Lab.__table__)

class Path(Base):
    __tablename__ = 'path'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False)
    config = Column(String(128))
    def __repr__(self):
        return '<path(name=%s)>'% self.name
        
print(Path.__table__)

#Base.metadata.create_all(engine)              

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
print(session.query(User).all())
#print(session.query(User).filter(User.name=='aiden').first())
user=session.query(User).first()
user1 = User(name='zhang',email='zhange@gmail.com')
session.add(user1)
session.commit()
user
print(user)
user=session.query(User).first()
user
user.email
user.name
user.id
user2 = User(name='ma',email='ma@hotmail.com')
session.add(user2)
session.commit()
user=session.query(User).all()
user[0].name
user[1].name

course1 = Course(name='python',teacher_id=2)
course2 = Course(name='linux',teacher_id=1)
session.add(course1)
session.add(course2)
session.commit()
course=session.query(Course).all()
course

lab1 = Lab(name='python object',course_id=1)
lab2 = Lab(name='linux bash',course_id=2)
session.add(lab1)
session.add(lab2)
session.commit()
lab=session.query(Course).all()

path1 = Path(name='python',config="{'description':'Python Path'}")
path2 = Path(name='linux',config="{'description':'Linux Path'}")
session.add(path1)
session.add(path2)
session.commit()
path=session.query(Path).all()
