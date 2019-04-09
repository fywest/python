# coding: utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server='localhost'
ip='220.181.57.216'
s.settimeout(5)

def pscan(port):
    try:
        s.connect((ip,port))
        return True
    except:
        return False

for x in range(79,85):
    if pscan(x):
        print('Port',x,'is open!!!!!!!!!')
    else:
        print('Port',x,'is closed')
