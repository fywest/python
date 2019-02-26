import copy

def compute(base,value):
    new_list=copy.deepcopy(base)
    new_list.append(value)
    result=sum(new_list)
    print(result)

if __name__=='__main__':
    testlist=[10,20,30]
    compute(testlist,15)
    compute(testlist,25)
    compute(testlist,35)
