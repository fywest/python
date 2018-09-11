# class Complex:
#     def __init__(self,real,image):
#         self.r=real
#         self.i=image
#
# a=Complex(3.0,-4.5)
#
# print(a.r,a.i)

# class Person(object):
#     def __init__(self,name):
#         self.name=name
#
#     def get_details(self):
#         return self.name
#
# class Student(Person):
#     def __init__(self,name,branch,year):
#         Person.__init__(self,name)
#         self.brance=branch
#         self.year=year
#
#     def get_details(self):
#         return "{} studies {} and is in {} year ".format(self.name,self.brance,self.year)
#
# class Teacher(Person):
#     def __init__(self,name,papers):
#         Person.__init__(self,name)
#         self.papers=papers
#
#     def get_details(self):
#         return "{} teaches {} ".format(self.name,','.join(self.papers))
#
# person1=Person("Sachin")
# student1=Student("Kushal",'CSE',2005)
# teacher1=Teacher('Parshad',['C','Python'])
#
# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())

# class Account(object):
#     def __init__(self,rate):
#         self._amt=0
#         self.rate=rate
#     @property
#     def amount(self):
#         return self._amt
#
#     @property
#     def cny(self):
#         return self._amt*self.rate
#
#     @amount.setter
#     def amount(self,value):
#         if value<0:
#             print("Sorry,no negative in account")
#             return
#         self._amt=value
#
# if __name__=='__main__':
#     acc=Account(rate=6.6)
#     acc.amount=20
#     print("Dollar amount:",acc.amount)
#     print("In CNY:",acc.cny)
#     acc.amount=100
#     print("Dollar amount:",acc.amount)
#     print("In CNY:",acc.cny)

#######################################################
# def starbar(num):
#     print('*'*num)
#
# def hashbar(num):
#     print('#'*num)
#
# def simplebar(num):
#     print('-'*num)

#################################################
# import requests
#
# req=requests.get('https://github.com')
# print(req.headers)
# print(req.status_code)

# import os
# import os.path
# import requests
#
# def download(url):
#     req=requests.get(url)
#     if req.status_code==404:
#         print("no such file found at %s" % url)
#         return
#     filename=url.split('/')[-1]
#     with open(filename,'wb') as fobj:
#         fobj.write(req.content)
#     print("Download over.")
#
# if __name__=='__main__':
#     url="http://www.xiaodian360.com"#input('Enter a URL')
#     download(url)

###############################################################
#import collections

# print(help(collections.Counter))
# from collections import Counter
# import re
#
# path='xiaodian360.txt'
# words=re.findall('\w+',open(path).read().lower())
# print(Counter(words).most_common(10))
# c=Counter(li=3,ma=2)
# print(list(c.elements()))

# from collections import defaultdict
# s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',5)]
# d=defaultdict(list)
# for k,v in s:
#     d[k].append(v)
# print(d.items())

# from collections import namedtuple
# Point=namedtuple('Point',['x','y'])
# p=Point(10,y=20)
# print(p)
# print(p.x+p.y)
# print(p[0]+p[1])
# x,y=p
# print(x,y)

