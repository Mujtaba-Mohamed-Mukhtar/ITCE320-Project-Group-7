import socket

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as Client_socket:
    Client_socket.connect(ServerAddress)
    print('='*15,'Client is ready','='*15,'\n')

    Name = input('User Name: ')