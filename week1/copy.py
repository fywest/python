#!/usr/bin/env python3

import sys

def copy_file(src,des):
    with open(src,'r') as src_file:
        with open(des,'w') as des_file:
            for src_line in src_file.readlines():
                des_file.write(src_line)

if __name__=='__main__':
    if len(sys.argv)<3:
        print("please input source and destiny files name")
        sys.exit(-1)
    for i,x in enumerate(sys.argv):
        if (i==0):
            continue
        print(i,x)
    copy_file(sys.argv[1],sys.argv[2])
    print('it is done')
    sys.exit(0)


