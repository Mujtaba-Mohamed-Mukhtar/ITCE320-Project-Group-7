import requests
import json
import socket
import time

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

print('='*15,'Server is ready','='*15)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress)
    Server_socket.listen()