num=input('please input number : ')

try:
    if num=='abc':
        raise ValueError
    elif not num.isdigit():
        raise NameError
    else:
        new_num=int(num)
        print('INT:{}'.format(new_num))
except ValueError:
    print("ERROR:abc")
except NameError:
    print("name error")
finally:
    print("it is done")



