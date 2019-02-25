fileName='/home/fywest/git/python/week1/nothing.txt'

f=open(fileName,'a')
try:
    f.write("louplus add\n")
except:
    print('file write error')
finally:
    print("finally!")
    f.close()
