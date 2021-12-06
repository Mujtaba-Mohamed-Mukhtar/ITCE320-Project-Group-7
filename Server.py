import requests
import json
import socket
import threading
import time

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

print('='*15,'Server is ready','='*15,'\n\n')



def connection (socket, address):

    Name = socket.recv(BufferSize).decode(Encoding)

    print('='*5,Name,'is connected','='*5,'\n')

    option = int(socket.recv(BufferSize).decode(Encoding))

    if option == 1:

        parameters = {
            'access_key':'4baf73cdfd1b2df1df2d86d704789801',
            'flight_status':'landed',
            'limit': 5
        }

        api_result = requests.get('http://api.aviationstack.com/v1/flights',parameters)

        if api_result.status_code != 200:
            print('error')


        with open('group_7.json','w') as file:

            json.dump(api_result.json(), file, indent=3)





with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress) #Creating the server socket and assigning IP address and port number
    Server_socket.listen()
    socket_A, Address = Server_socket.accept()

    thread1 = threading.Thread(target=connection, args=(socket_A, Address))
    thread1.start()


