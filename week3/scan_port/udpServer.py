import socket

def main():
    ip='127.0.0.1'
    port=5000

    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip,port))

    print ("Server Started")
    while True:
        data,addr=s.recvfrom(1024)
        print (f'message from: {str(addr)}')
        print (f'from connected user: {str(data)}')
        data=str(data).upper()
        print (f'sending : " {str(data)}')
        s.sendto(data.encode("utf-8"),addr)
    c.close()

if __name__=='__main__':
    main()
