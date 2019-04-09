# coding: utf-8
import socket

s=socket.socket()
host=socket.gethostname()
port=12346
s.bind((host,port))

s.listen(5)
while True:
    c,addr = s.accept()
    print('conect addr: ',addr)
    c.send('welcome!'.encode('utf-8'))
    c.close()
