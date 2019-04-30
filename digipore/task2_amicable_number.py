#!/usr/bin/env python3


def sum_divisors(num):
    sum_val = 0
    for i in range(1, int(num/2+1)):
        if (num % i == 0):
            sum_val += i
    return sum_val


if __name__ == '__main__':

    val = 0
    sum_val = 0
    try:
        val = int(input("input number : "))
    except (ValueError, NameError):
        print("please input integer value")
        exit(1)

    print('input value is {0}'.format(val))
    sum_amicable = 0
    for i in range(1, val):
        sum_a = 0
        sum_b = 0
        sum_a = sum_divisors(i)
        sum_b = sum_divisors(sum_a)
        if sum_b > sum_a and sum_a != i and sum_b == i:
            # print(sum_a,sum_b,i)
            sum_amicable += sum_a+sum_b

    print('sum of all amicable value are  {0}'.format(sum_amicable))
