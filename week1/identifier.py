import sys
import keyword

name=sys.argv[1]
if (not name[0].isalpha()) and (name[0]!='_'):
    print("wrong name for python")
elif keyword.iskeyword(name):
    print("name can not be same with keyword")
else:
    print("it is right name")


