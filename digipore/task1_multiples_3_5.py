#!/usr/bin/env python3
import sys


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

    for i in range(1,val):
        print(i)
        if (i%3==0) or (i%5==0):
            print("'''",i)
            sum_val+=i
    print('sum value is {0}'.format(sum_val))

