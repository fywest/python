#!/usr/bin/env python3

if __name__ == '__main__':

    val = 0
    sum_val = 0
    try:
        val = int(input("input number :"))
    except (ValueError, NameError):
        print("please input integer value")
        exit(1)

    print('input value is {0}'.format(val))

    for i in range(1, val):
        if (i % 3 == 0) or (i % 5 == 0):
            sum_val += i
    print('sum value is {0}'.format(sum_val))
