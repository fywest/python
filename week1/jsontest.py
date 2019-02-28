import json

class Student(object):
    def __init__(self,user_id,name,pass_info,study_time):
        self._user_id=user_id
        self._name=name
        self._pass_info=pass_info
        self._study_time=study_time

    def __repr__(self):
        return "{0},{1},{2},{3}".format(self._user_id,self._name,self._pass_info,self._study_time)

def obj_dict(obj):
    return obj.__dict__

if __name__=='__main__':
    student1=Student(1000,'Shiyan',10,50)
    student2=Student(2000,'Lou',15,171)
    print(student1)
    print(student2)
    students=[]
    students.append(student1)
    students.append(student2)
    print(students)
    s=json.dumps(student1.__dict__)
    print(s)
    with open('jsontest.json','w') as f:
            f.write(json.dumps(students,default=obj_dict))

    json_string=json.dumps([ob.__dict__ for ob in students])
    print(json_string)

    with open('jsontest1.json','w') as f:
        f.write(json_string)


