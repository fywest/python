#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import time

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',6999))

#conn,addr = server.accept()
#print(conn,addr)
i=0
while True:
    msg="welcome here ! {0}".format(i)
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print('recv',data.decode())
    i+=1
    time.sleep(1)
client.close()

        
