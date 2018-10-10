#!/usr/bin/env python3

import sys
from collections import Counter


class Person(object):

    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

    def get_grade(self, grade):
        print(grade)


class Student(Person):

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):

        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self, grade):

        c = Counter(grade)
        grade_list = c.most_common(4)
        num_pass, num_fail = 0, 0
        for i, pari in enumerate(grade_list):
            if pari[0] in ['A', 'B', 'C']:
                num_pass += pari[1]
            else:
                num_fail += pari[1]
        print("pass: {},fail: {}".format(num_pass, num_fail))


class Teacher(Person):

    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self, grade):
        c = Counter(grade)
        grade_list = c.most_common(4)
        list_len = len(grade_list)
        for i, pari in enumerate(grade_list):
            if i != list_len - 1:
                print("{}: {}, ".format(pari[0], pari[1]), end='')
            else:
                print("{}: {}".format(pari[0], pari[1]))


if __name__ == '__main__':

    person1 = Person('Sachin')
    student1 = Student('Kushal', 'CSE', 2005)
    teacher1 = Teacher('Prashad', ['C', 'C++'])

    if len(sys.argv) < 4:
        print("check command")
        exit(-1)
    role = sys.argv[3].lower()
    grade_input = sys.argv[4].upper()

    if role == 'teacher':
        teacher1.get_grade(grade_input)
    elif role == 'student':
        student1.get_grade(grade_input)
