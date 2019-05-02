#!/usr/bin/env python3

a=[1,3,5,7,9,12,2,4,6,8]
#a=[2,3,4,1]
list_combine=[]
list_set=set()
list_array=[]
list_result=[]
list_sum=[]


if __name__ == '__main__':
   
    
    for i in a:
        list_set.add(i)

    print("*******list set*********")
    print(list_set)

    for i in range(0,len(a)):
        temp_list=[]
        for j in range(i,len(a)):
            if i==j:
                continue
            #print('({0},{1}) '.format(a[i],a[j]),end=' ')
            temp=(a[i],a[j])
            temp_list.append(temp)
        #print(temp_list)
        #list_combine.append(temp_list)
        list_combine+=temp_list
    #print()
    #print(list_combine)    
    
    print("*******combine_list*********")
    for i in list_combine:
        print('{0}'.format(i),end=' ')
        #for j in i:
        #print('{0}'.format(i),end=' ')
    print(len(list_combine))
    
    print("*******list*********")

    length=len(list_combine)
    for i in range(0,length):
        for j in range(i,length):
            print(list_combine[j],end=' ')
        print()

    for i in range(0,length):
        print("iiiiiiiiiiiiiiiiiiiiiii",i)
        temp_set=set()
        temp_list=[]
        temp=i
        second_status=False
        i_tuple=list_combine[i]
        for j in range(i,length):
            print("jjjjjjjjjjjjjjjjjjjjjj",j)
            #print(j,list_combine[j])
            j_tuple=list_combine[j]
            print(j,j_tuple,j_tuple[0],j_tuple[1])
            
            if(j_tuple[0] not in temp_set) and  (j_tuple[1] not in temp_set ):
                temp_set.add(j_tuple[0]) 
                temp_set.add(j_tuple[1]) 
                temp_list.append(j_tuple)
                print("fffffffffffffffffff not in temp set ffffff",temp_list) 
                
                if temp_set==list_set:
                    print(temp_set,list_set)
                    print("ffffffffffffffffffffff temp_set== list_set")

                    list_result.append(temp_list)
                    #del temp_list[:]
                    temp_list=[]
                    temp_set.clear()
                    second_status=False
                    

                    
                    temp_set.add(i_tuple[0]) 
                    temp_set.add(i_tuple[1]) 
                    temp_list.append(i_tuple)

                    j=temp+1

                if(i!=j and second_status==False):
                    temp=j
                    second_status=True

            print(temp_list)
            print(temp_set)
            print(second_status)

            
                


        print(list_result)

    print("*******result_list*********")
    for item in list_result:
        result=0
        for i in item:
            result+=min(i[0],i[1])
            print('{0}'.format(min(i[0],i[1])),end=' ')
        print(item)
        list_sum.append(result)
    print(list_sum)

    print("*******combine_list*********")
    for i in list_combine:
        print('{0}'.format(i),end=' ')
        #for j in i:


    '''
    for i in range(0,10):
        print(list_combine[i])

    show_tuple(list_combine,0)
    '''
    '''
    print("*******add list*********")
    add_list(list_combine,0,0)
    print(list_array)
    '''

    '''
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

    '''
