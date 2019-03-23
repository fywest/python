# coding: utf-8
from sqlalchemy import create_engine
engine = create_engine('mysql://root:990113@localhost/shiyanlou')
engine.execute('select * from user').fetchall()
get_ipython().run_line_magic('env', '')
get_ipython().run_line_magic('pwd', '')
