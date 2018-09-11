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
        pass

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
        print(grade)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        pass

if __name__=='__main__':

    person1 = Person('Sachin')
    student1 = Student('Kushal', 'CSE', 2005)
    teacher1 = Teacher('Prashad', ['C', 'C++'])

    # print(person1.get_details())
    # print(student1.get_details())
    # print(teacher1.get_details())

    if len(sys.argv)<1:
        print("check command")
        exit(-1)
    print(sys.argv[1])
    print(student1.get_grade(sys.argv[1]))