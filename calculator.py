#!/usr/bin/env python3
import sys


def calculate(salary):
    insurance = 0
    start = 3500
    if salary < start:
        return 0
    money_tax = salary - insurance - start
    if money_tax > 80000:
        rate_tax = 0.45
        reduce_tax = 13505
    elif money_tax > 55000:
        rate_tax = 0.35
        reduce_tax = 5505
    elif money_tax > 35000:
        rate_tax = 0.30
        reduce_tax = 2755
    elif money_tax > 9000:
        rate_tax = 0.25
        reduce_tax = 1005
    elif money_tax > 4500:
        rate_tax = 0.20
        reduce_tax = 555
    elif money_tax > 1500:
        rate_tax = 0.10
        reduce_tax = 105
    else:
        rate_tax = 0.03
        reduce_tax = 0

    return money_tax * rate_tax - reduce_tax


if len(sys.argv) != 2:
    print("Parameter Error")
    sys.exit(1)

if __name__ == '__main__':
    input_num = ''
    try:
        input_num = sys.argv[1]
        if input_num.isdigit():
            print("{:.2f}".format(calculate(int(input_num))))
            sys.exit(0)
        else:
            raise ValueError
    except ValueError:
        print("Parameter Error")
        sys.exit(1)
