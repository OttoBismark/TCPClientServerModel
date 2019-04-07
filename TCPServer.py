import socket

# Main function
def Main():
    host = '127.0.0.1' #Server Address
    port = 5000 #Server port

    s = socket.socket() #Creating a socket for instanciate a communication
    s.bind((host, port)) #Bring the host and port into a process

    s.listen(1) #Calling the listen function

    c, addr = s.accept() #Calling the accepting communication from
                         # other client's requests

    print("Connection from : " + str(addr))

    while True:
        # Recevie data from
        data = c.recv(1024)
        if not data:
            break

        print("From connected user: " + str(data))
        data = str(data).upper()
        print("Sending... " + str(data))
        c.sendall(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()
