#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',6999))

while True:
#conn,addr = server.accept()
#print(conn,addr)
    while True:
        msg="welcome here !"
        client.send(msg.encode('utf-8'))
        data=client.recv(1024)
        print('recv',data.decode())
    client.close()

        
