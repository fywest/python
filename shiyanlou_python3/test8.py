# def change():
#     global a
#     a=90
#     print(a)
#
# a=9
#
# print("before",a)
# print("inside change",end=" ")
# change()
# print("After ",a)

def f(a,data=[]):
    data.append(a)
    return data

# print(f(1,[6,8]))
# print(f(2))
# print(f(3))
#
# def f1(a,data=None):
#     if data is None:
#         data=[]
#     data.append(a)
#     return data
#
# print(f1(1))
# print(f1(2))
# print(f1(3))