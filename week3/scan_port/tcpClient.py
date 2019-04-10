import socket

def main():
    ip='127.0.0.1'
    port=5000

    s=socket.socket()
    s.connect((ip,port))

    message =input("->")
    while message !='q' :
        s.send(message.encode("utf-8"))
        data=s.recv(1024)
        print(f"Received from server : {str(data)}")
        message = input("->")
    c.close()

if __name__=='__main__':
    main()

