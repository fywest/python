#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6999))
server.listen(5)

while True:
    conn,addr = server.accept()
    print(conn,addr)
    while True:
        try:
            data=conn.recv(1024)
            print('recive:',data.decode())
            conn.send(data.upper())
        except ConnectionResetError as e:
            print('close connection')
            break
    conn.close()
