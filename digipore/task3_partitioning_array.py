#!/usr/bin/env python3
import itertools

# a = [1, 3, 5, 7, 9, 12, 2, 4, 6, 8]
# b = [-3, 1, 4, 3, 2, -4]
list_sum = []
list_max = []
max_value = -10000
max_tuple = ()

if __name__ == '__main__':
    print("Please enter even numbers of elements separated by space ")
    try:
        input_string = input("input value :")

        c = [int(i) for i in input_string.split()]
    except (ValueError, NameError):
        print("please input integer value")
        exit(1)

    if len(c) % 2 != 0 or len(c) == 0:
        print("please input even numbers of elements")
        exit(1)

    print("input:{}".format(c))
    num = 0
    for item in itertools.permutations(c, len(c)):
        num += 1
        count = 0
        temp = 0
        list_temp = []
        list_result = []
        for i in item:
            count += 1
            if count % 2:
                temp = i
            else:
                tmp_tuple = (temp, i)
                list_temp.append(tmp_tuple)
                list_result.append(min(tmp_tuple))
        value = sum(list_result)
        if value > max_value:
            list_max = list_result
            max_value = value
            max_tuple = item

        list_sum.append(sum(list_result))

    print("output:{0}".format(max(list_sum)))
