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

# def f(a,data=[]):
#     data.append(a)
#     return data

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

#fobj=open("sample.txt")
#print(fobj.read())

# print("-",fobj.readline())
# print("-",fobj.readline())
# print("-",fobj.readline())

# print("-",fobj.readlines())

# for x in fobj:
#     print(x,end="")
#
#
# fobj.close()


# fobj=open("ircnicks.txt",'w')
# fobj.write('powerpork\n')
# fobj.write('indrag\n')
# fobj.write('mishtin\n')
# fobj.write('sankarshan\n')
# fobj.close()
#
# fobj=open("ircnicks.txt",'r')
# s=fobj.read()
# fobj.close()
# print(s)


#
# import sys
# if len(sys.argv)<3:
#     print("wrong parameter")
#     print("copyfile.py file1 file2")
#     sys.exit()
# for i,x in enumerate(sys.argv):
#     print(i,x)
# f1=open(sys.argv[1])
# s=f1.read()
# f1.close()
#
# f2=open(sys.argv[2],'w')
# f2.write(s)
# f2.close()

############################################
# import os
# import sys
#
# def parse_file(path):
#     fd=open(path)
#     i,spaces,tabs=0,0,0
#     for i,line in enumerate(fd):
#         spaces+=line.count(' ')
#         tabs+=line.count('\t')
#     fd.close()
#     return spaces,tabs,i+1
#
# def main(path):
#     if os.path.exists(path):
#         spaces,tabs,lines=parse_file(path)
#         print("Space {} Tabs {} Lines {}".format(spaces,tabs,lines))
#         return True
#     else:
#         return False
#
# #2tabst     t
# if __name__=='__main__':
#     if len(sys.argv)>1:
#         print(sys.argv)
#         main(sys.argv[1])
#     else:
#         sys.exit(-1)
#     sys.exit(0)
#################################################

# with open('sample.txt') as fobj:
#     for line in fobj:
#         print(line,end='')


#below for ubuntu
# with open('/proc/cpuinfo') as f:
#     for line in f:
#         print(line)


#################################################
# def get_number():
#     "Returns a float number"
#     number=float(input("enter a float number"))
#     if number >0 and number <1:
#         raise ValueError("value between 0 and 1")
#     return number
#
# while True:
#     try:
#         print(get_number())
#     except ValueError:
#         print("not float number ,try again")
#     finally:
#         print("good bye")

#####################################################