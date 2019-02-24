import sys

print('now __name__ value is: {}'.format(__name__))
for arg in sys.argv[1:]:
    if len(arg)>2:
        print(arg)


