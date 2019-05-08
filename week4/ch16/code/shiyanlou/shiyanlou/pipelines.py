# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine, User, Repository
from scrapy.exceptions import DropItem

from shiyanlou.items import CourseItem, UserItem ,RepositoryItem
from datetime import datetime

class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        elif isinstance(item, UserItem):
            self._process_user_item(item)
        elif isinstance(item, RepositoryItem):
            self._process_user_item(item)
        
        
        return item
    
    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        item['name'] = str(item['name']).strip()
        item['description'] = str(item['description']).strip()
        item['type'] = str(item['type']).strip()
        if item['students'] < 1000:
            raise DropItem('Course studens less thant 1000.')
        else:   
            self.session.add(Course(**item))
        return item

    def _process_user_item(self, item):
        item['name']=item['name']
        item['join_date']=datetime.strptime(item['join_date'], '%Y-%m-%d').date()
        item['learn_courses_num']=int(item['learn_courses_num'])

        self.session.add(User(**item))

    def _process_repository_item(self, item):
        item['name']=item['name']
        item['update_date']=datetime.strptime(item['update_date'], '%Y-%m-%d').date()

        self.session.add(User(**item))



    def open_spider(self, spider):
        
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def close_spider(self, spider):
        
        self.session.commit()
        self.session.close()
