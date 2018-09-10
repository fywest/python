# a=[23, 45, 1, -3434, 43624356, 234]
# print(a)
# a.append(45)
# print(a)
# a.insert(0,1)
# a.insert(0,111)
# print(a)
# print(a.count(45))
# a.remove(234)
# print(a)
# a.reverse()
# print(a)
# b=[45, 56, 90]
# a.extend(b)
# print(a)
# a.sort()
# print(a)
# del a[-1]
# print(a)

# a=[1, 2, 3, 4, 5, 6]
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# a.pop()
# print(a)
# a.append(34)
# print(a)
# a.remove(6)
# print(a)
# a.append(1)
# print(a)
# a.pop(0)
# a.pop(0)
# print(a)

#squares=list(map(lambda x:x**2, range(10)))
# squares=[x**2 for x in range(10)]
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# a=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
# print(a)

# a=[1,2,3]
# z=[x+1 for x in [x**2 for x in a]]
# print(z)

# a='Fedora', 'Shiyanlou', 'Kubuntu', 'Pardus'
# print(a)
# print(a[0])
# for x in a:
#     print(x,end=' ')

# x,y=divmod(15,2)
# print(x,y)

# a=(123)
# print(type(a))
#
# a=(123,)
# print(type(a))

# basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
#
# print('orange' in basket)
# a=set('abracadabra')
# b=set('alacazam')

# print(a)
# print(b)
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)

# a={'a', 'e', 'h', 'g'}
# print(a)
# a.pop()
# print(a)
# a.add('c')
# print(a)


#dictionary
# data={'kushal':'Fedora','kart_':'Debian','Jace':'Mac'}
# print(data)
# print(data['kart_'])
# del data['kushal']
# print(data)
# print('Jace' in data)

# a=dict((('indian','Delhi'),('Bangladesh','Dhaka')))
# print(a)

# data={'kushal':'Fedora','kart_':'Debian','Jace':'Mac'}
# for key,value in data.items():
#     print("{} users {}".format(key,value))

# data={1:2}
# print(type(data))

# data={}
# data.setdefault('names',[]).append('Ruby')
# print(data)
# data.setdefault('names',[]).append('Python')
# print(data)

# data={}
# data['foo']=5
# print(data.get('foo',0))

# a=['a', 'b', 'c']
# for i,j in enumerate(a):
#     print(i,j)

# n=int(input("enter number of students"))
# data={}
# subjects=('Physics','Maths','History')
# for i in range(0,n):
#     name=input("enter name of student {}".format(i+1))
#     marks=[]
#     for x in subjects:
#         marks.append(int(input("enter marks of {}:".format(x))))
#     data[name]=marks
# for x,y in data.items():
#     total=sum(y)
#     print("{}'s total marks {}".format(x,total))
#     if total<120:
#         print(x," failed :(")
#     else:
#         print(x,"pass :)")


#string
# s="shi yan lou"
# print(s.title())
# z=s.upper()
# print(z)
# z.lower()
# print(z.lower())
# s="I am A pRoGraMMer"
# print(s.swapcase())
# print("jdwb 234jb".isalnum())
# print("jdwb234jb".isalnum())
# print("jdwb".isalpha())
# print("1245".isdigit())
# print("CHINA".isupper())

# s="We all love Python"
# z=s.split()
# print(z)
# j="-".join(z)
# print(j)

# print("---")
# a=" a bc\n "
# print(a)
# print("---")
# print(a.strip())
# print("---")
# print(a)
# print("---")

# s="faulty for a reason"
# print(s.find("for"))
# print(s.find("fora"))
# print(s.startswith("fa"))
# print(s.endswith("son"))

# s="input sentents which is funny"
# z=s[::-1]
# print(s)
# print(z)
#
# count=len(s.split(" "))
# print(count)

