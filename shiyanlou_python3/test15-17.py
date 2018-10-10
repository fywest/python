# class Counter(object):
#     def __init__(self,low,high):
#         self.current=low
#         self.high=high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current>self.high:
#             raise StopIteration
#         else:
#             self.current+=1
#             return self.current-1
#
#
# c=Counter(5,10)
# for i in c:
#     print(i,end=' ')
#
# d=Counter(5,6)
# print(next(d))
# print(next(d))
# print(next(d))

#############################################
# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
# fun=my_generator()
# print(fun)
#
# for char in my_generator():
#     print(char)

#############################################

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before call")
#         name=input("what is your name")
#         result=func(*args,**kwargs)
#         print("after call")
#         print("{} finnished".format(name))
#         return result
#     return wrapper
#
# @my_decorator
# def add(a,b):
#     return a+b
#
# print(add(1,3))

###############################################
# import unittest
# from factorial import fact
#
# class TestFactorial(unittest.TestCase):
#     def test_fact(self):
#         res=fact(5)
#         self.assertEqual(res,120)
#
# if __name__=='__main__':
#     unittest.main()

################################################
import unittest
from factorial import fact, div

class TestFactorial(unittest.TestCase):
    def test_fact(self):
        res=fact(5)
        self.assertEqual(res,120)

    def test_error(self):
        self.assertRaises(ZeroDivisionError,div,0)

if __name__=='__main__':
    unittest.main()
