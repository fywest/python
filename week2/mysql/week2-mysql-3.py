# coding: utf-8
from sqlalchemy import create_engine

engine = create_engine('mysql://root:990113@localhost/shiyanlou',echo=True)

print(engine.execute('select * from user').fetchall())
#print(get_ipython().run_line_magic('env', ''))
print(get_ipython().run_line_magic('pwd', ''))

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
    
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
print(session.query(User).all())
print(session.query(User).filter(User.name=='aiden').first())
