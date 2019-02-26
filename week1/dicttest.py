import sys

print(sys.argv)
dicttest={}
for pair in sys.argv[1:]:
    key,value=pair.split(':')
    dicttest[key]=value

for key,value in dicttest.items():
    print('ID:{} Name:{}'.format(key,value))
