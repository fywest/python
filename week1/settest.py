import sys

print(sys.argv)
settest=set()
if len(sys.argv)>1:
    for item in sys.argv[1:]:
       settest.add(item)
    print(settest)

else:
    print("please input parameters")
