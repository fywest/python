#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import socket

def main():
    if len(sys.argv)<5:
        print("Parameter Error")
        exit(1)
    command_list=sys.argv[1:]
    ip_index=command_list.index('--host')
    ip=command_list[ip_index+1]

    pattern=re.compile("^\d+.\d+.\d+.\d+$")
    if pattern.fullmatch(ip)==None:
        print("Parameter Error")
        exit(1)

    port_index=command_list.index('--port')
    try:
        port_list=[int(item.strip()) for item in command_list[port_index+1].split('-')]
    except ValueError:
        print("Parameter Error")
        exit(1)
    get_port(ip,port_list)


def get_port(ip,port_list):
    if len(port_list)==1:
        if pscan(ip,port_list[0]):
            print('open')
        else:
            print('close')
    else:
        for num in range(port_list[0],port_list[1]+1):
            #print(ip,num)
            if pscan(ip,num):
                print(f'{num} open')
            else:
                print(f'{num} closed')
            
    
def pscan(ip,port):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.settimeout(2)

    try:
        client.connect((ip,port))
        client.close()

        return True
    except:
        client.close()
        return False

if __name__=='__main__':
    main()
    #ip='220.181.57.216'
    #port=80
