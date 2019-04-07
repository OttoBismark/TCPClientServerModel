import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    # message = raw_input("-> ")
    message = input("-> ")

    while message != 'q':
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print("Received from server: " + str(data))
        # message = raw_input("->" )
        message = input("-> ")
    s.close()

if __name__ =='__main__':
    Main()
