# coding: utf-8
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

