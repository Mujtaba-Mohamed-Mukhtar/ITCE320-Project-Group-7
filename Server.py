import requests
import json
import socket
import threading
import time

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

print('='*15,'Server is ready','='*15)



def connection (socket, address):

    Name = socket.recv(BufferSize).decode(Encoding)

    print('='*5,Name,'is connected','='*5)



with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress) #Creating the server socket and assigning IP address and port number
    Server_socket.listen()
    socket_A, Address = Server_socket.accept()

    thread1 = threading.Thread(target=connection, args=(socket_A,Address))


    