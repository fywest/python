#!/usr/bin/env python3
import itertools

a=[1,3,5,7,9,12,2,4,6,8]
b=[-3,1,4,3,2,-4]
c=[2]
list_sum=[]
list_max=[]
max_value=-1000
max_tuple=()

if __name__=='__main__':
    num=0 
    a1=0
    a2=0
    for item in itertools.permutations(b,len(b)):
        print(item)
        num+=1
        count=0
        temp=0
        list_temp=[]
        list_result=[]
        for i in item:
            count+=1
            if count%2:
                temp=i
            else:
                tmp_tuple=(temp,i)
                list_temp.append(tmp_tuple)
                list_result.append(min(tmp_tuple))
        print(list_temp)
        print(list_result)
        print(sum(list_result))
        value=sum(list_result)
        if value > max_value:
            list_max=list_result
            max_value=value
            max_tuple=item

        list_sum.append(sum(list_result))
            
        #break
    print(num)
    print(list_sum)
    print(max(list_sum))
    print(list_max)
    print(max_tuple)
    print(max_value)


