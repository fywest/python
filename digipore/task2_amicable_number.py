#!/usr/bin/env python3
import sys



def sum_divisors(num):
    sum_val=0
    for i in range(1,num):
        if (num%i==0):
            sum_val+=i
#print('sum value is {0}'.format(sum_val))
    return sum_val

if __name__ == '__main__':
#num_range=int(sys.argv[0])
    val=0
    sum_val=0
    user_input=input("input number :")
    try:
        val = int(user_input)
    except ValueError:
        print("please input integer value")
        exit(1)

    print('input value is {0}'.format(val))
    sum_amicable=0
    for i in range(1,val):
        sum_a=0
        sum_b=0
        sum_a=sum_divisors(i)
        sum_b=sum_divisors(sum_a)
        if sum_b>sum_a and sum_a!=i and sum_b==i:
            print(sum_a,sum_b,i)
            sum_amicable+=sum_a+sum_b

    print('sum of all amicable value are  {0}'.format(sum_amicable))



