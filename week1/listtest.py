import sys

items_LTE3=[]
items_BT3=[]
for parameter in sys.argv[1:]:
    print(parameter)
    if len(parameter)<=3:
        items_LTE3.append(parameter)
    else:
        items_BT3.append(parameter)

print(items_LTE3)
print(items_BT3)
    


