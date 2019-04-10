import socket

def main():
#host='www.sina.com.cn'
    host='www.cnn.com'
    port=80

    s=socket.socket()
    s.connect((host,port))
#message='GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'
    message='GET / HTTP/1.1\nHost: www.cnn.com\n\n'
    s.sendall(message.encode("utf-8"))

    buffer=[]
    while True:
        d=s.recv(1024)
        if d:
            buffer.append(str(d))
        else:
            break
    data = ' '.join(buffer)
    s.close()
    
    print(data)
#header, html = data.split('\r\n\r\n',1)
    #header, html = data.split('\r\n',1)
#print (header)

    with open('sina.html','wb') as f:
        f.write(data.encode('utf-8'))

if __name__=='__main__':
    main()

