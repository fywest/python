# coding: utf-8
session.close()
course=session.query(Course).first()
course.tags
tag1=Tag(name='tag_1')
tag2=Tag(name='tag_2')
course.tags.append(tag1)
course.tags.append(tag2)
session.add(course)
session.commit()
course.tags
engine.execute('select * from tag').fetchall()
engine.execute('select * from course_tag').fetchall()
teacher = session.query(User).filter(User.name=='zhang').first()
teacher
course1=Course(name='linux',teacher=teacher)
course1
session.add(course1)
session.commit()
tag1.courses
tag1.courses.append(course1)
session.add(tag1)
session.commit()
tag1.courses
