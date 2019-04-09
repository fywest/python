# coding: utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s
server='pythonprogramming.net'
port=80
server_ip=socket.gethostbyname(server)
server_ip
request="GET / HTTP/1.1\nHost: "+server+"\n\n"
s.connect((server,port))
s.send(request.encode())
result=s.recv(4096)
result
