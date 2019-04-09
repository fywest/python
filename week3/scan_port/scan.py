#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(1)

def pscan(ip,port):
    try:
        client.connect((ip,port))
#client.connect(('220.181.57.216',80))
        client.close()
        return True
    except:
        client.close()
        return False

'''
for port in range(80,85):
    ip='localhost'
    if pscan(ip,port):
        print('Port',port,'is open!!!!!!!!!')
    else:
        print('Port',port,'is closed')
'''
if __name__=='__main__':
    if len(sys.argv)<5:
        print("Parameter Error")
        exit(1)
    command_list=sys.argv[1:]
    ip_index=command_list.index('--host')
    ip=command_list[ip_index+1]
    port_index=command_list.index('--port')
#port=int(command_list[port_index+1])
    port_list=[int(item.strip()) for item in command_list[port_index+1].split('-')]

#ip='220.181.57.216'
#port=80
    print(port_list)
    if len(port_list)==1:
        if pscan(ip,port_list[0]):
            print('open')
        else:
            print('close')
    else:
        for num in range(port_list[0],port_list[1]+1):
            print(ip,num)
            if pscan(ip,num):
                print('open')
            else:
                print('close')
            
