# import math
# print(math.e)

# number=int(input("enter a integer: "))
# if number < 100:
#     print("number is {} and it is less than 100".format(number))
# else:
#     print("number is {} and it is not less than 100".format(number))

# amount=10000#float(input("enter amount: "))
# rate=0.14#float(input("enter rate: "))
# period=5#int(input("enter period"))
#
# value=0
# year=1
#
# while year<=period:
#     amount=amount*(rate+1)
#     print("Year {} Rs. {:.2f}".format(year,amount))
#     year+=1

# import math
# a=5
# b=-4
# c=0
#
# d=b*b-4*a*c
# if d<0:
#     print("roots are imaginary")
# else:
#     root1=(-b+math.sqrt(d))/(2*a)
#     root2 = (-b - math.sqrt(d)) / (2 * a)
#     print("root1 = ",root1)
#     print("root2 = ", root2)

# x=int(input("enter a number"))
#
# if x==0:
#     print("zero")
# elif x<0:
#     print("negtive")
# else:
#     print("positive")

#Fibonacci
# a,b=0,1
# while b<100:
#     print(b,end=' ')
#     a,b=b,a+b
    # temp=a
    # a=b
    # b=temp+b

#e^x=1+x+x^2/2!+x^3/3! (0<x<1)
# x=0.5#float(input("enter value of x: "))
# n=term=num=1
# result=1.0
#
# while n<100:
#     term*=x/n
#     result+=term
#     print("n={} x={:.5f} term={:.5f} result={:.5f}".format(n,x,term,result))
#     n+=1
#     if term<0.0001:
#         break
# print("No of Times= {} and Sum= {}".format(n,result))


# i=1
# print("-"*50)
# while i<11:
#     n=1
#     while n<=10:
#         print("{:4d}".format(i*n),end=' ')
#         n+=1
#     print()
#     i+=1
# print("-" * 50)

#a=[1,342,223,'india','Fedora']
# print(a)
# print(a[0])
# print(a[-1])
# print(a[0:2])
# print(a[:-2])
# print(a[-2:])
# print(a[1::2])
#b=[36,49,64,81,100]
# print(a+b)
# print('india' in a)
# print(342 in a)
# print(len(a))
# for i in a:
#     print(i,end=' ')
#
# for i in range(5):
#     print(i)
