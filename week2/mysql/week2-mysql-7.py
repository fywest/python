# coding: utf-8
pourse = session.query(Course).first()
course = session.query(Course).all()
course
course = session.query(Course).first()
course
lab1=Lab(name='ORM basic',course_id=course.id)
lab2=Lab(name='relation db',course=course)
session.add(lab1)
session.add(lab2)
session.commit()
course.labs
course.name
lab1.course
course.name='Python data analysis'
session.add(course)
session.commit()
lab1.course
session.query.all()
session.query(Course).all()
course.labs
session.delete(lab1)
session.commit()
course.labs
