#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        print("person")

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self,grade):

        print(len(grade),grade)
        c=Counter(grade)
        list=c.most_common(4)
        print(type(list))
        print(list)
        list_len=len(list)
        num_pass,num_fail=0,0
        for i,pari in enumerate(list):
            if pari[0] in ['A','B','C']:
                num_pass+=pari[1]
            else:
                num_fail+=pari[1]
        print("pass: {},fail: {}".format(num_pass,num_fail))





class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self,grade):
        c=Counter(grade)
        list=c.most_common(4)
        list_len=len(list)
        for i,pari in enumerate(list):
            if i != list_len-1:
                print("{}: {}, ".format(pari[0],pari[1]),end='')
            else:
                print("{}: {}".format(pari[0], pari[1]))


if __name__=='__main__':

    person1 = Person('Sachin')
    student1 = Student('Kushal', 'CSE', 2005)
    teacher1 = Teacher('Prashad', ['C', 'C++'])

    # print(person1.get_details())
    # print(student1.get_details())
    # print(teacher1.get_details())
    #ABCCBADDAA
    #print(sys.argv)
    if len(sys.argv)<4:
        print("check command")
        exit(-1)
    role=sys.argv[3].lower()
    grade=sys.argv[4].upper()
    #print(role,grade)

    if  role== 'teacher':
        teacher1.get_grade(grade)
    elif role == 'student':
        student1.get_grade(grade)