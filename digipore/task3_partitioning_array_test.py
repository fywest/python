#!/usr/bin/env python3
import itertools

a=[1,3,5,7,9,12,2,4,6,8]
list_combine=[]
list_array=[]

def show_tuple(list_combine,n):
    if len(list_combine[n])==0:
        return 0
    print(list_combine[n])
    show_tuple(list_combine,n+1)



def add_list(list_temp,index,row):
    if len(list_temp[row])==0:
        return 0

    print(list_temp[row][index],end=" ")
    index+=1
    print(len(list_temp[row]),index,row)

    if len(list_temp[row])==index:
        row+=1
        index=0
        print()

#list_array.append(list_temp[0])
    add_list(list_combine,index,row)



if __name__ == '__main__':
    
    for i in range(0,10):
        for j in range(i,10):
            print('{0}'.format(a[j]),end=' ')
        print()
    for i in range(0,10):
        temp_list=[]
        for j in range(i,10):
            if i==j:
                continue
            print('({0},{1}) '.format(a[i],a[j]),end=' ')
            temp=(a[i],a[j])
            temp_list.append(temp)
        print(temp_list)
        list_combine.append(temp_list)
        print()
    print(list_combine)    
    for i in list_combine:
        for j in i:
            print('{0}'.format(j),end=' ')
        print()

    for i in range(0,10):
        print(list_combine[i])

    show_tuple(list_combine,0)

    print("*******add list*********")
    add_list(list_combine,0,0)
    print(list_array)

    
    '''
    for i in range(0,len(a)):
        print('{0}'.format(a[i]),end=' ')
        #tuple_1=(a[0],a[i])
        #print('{0}'.format(tuple_1),end=' ')
        #print() 
    print("********permutatons**********")
    print(list(itertools.permutations(a,2)))
    print("*******combinations*********")
    print(list(itertools.combinations(a,2)))
    list_combine=list(itertools.combinations(a,2))
    print(len(list_combine))
    print("*******looping*********")
    '''

