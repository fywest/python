#!/usr/bin/env python3
import sys

class Test:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __iter__(self):
        return self

    def __next__(self):
        self.a+=self.c
        if self.a > self.b:
            raise StopIteration()
        return self.a

if __name__=='__main__':
    if len(sys.argv)<4:
        print("please iput min and max and step value")
        exit(-1)
    test=Test(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

    for item in test:
        print(item)
    exit(0)
