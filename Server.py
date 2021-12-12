import requests
import json
import socket
import threading
import Functions




ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

print('=' * 15, 'Server is ready', '=' * 15, '\n\n')





def connection(socket, address):
    Name = socket.recv(BufferSize).decode(Encoding)
    print('=' * 5, Name, 'is connected', '=' * 5, '\n')




    params = {
        'access_key' : '843591f5114e7c7994823d002e7b6013',
        'limit' : 100
    }

    with open('group_7.json', 'w') as file:

        api_response = requests.get('http://api.aviationstack.com/v1/flights', params)
        if api_response.status_code != 200:
            print('!' * 5, 'Request error')

        json.dump(api_response.json(), file, indent=3)



    option = 0

    while True:

        try:
            option = int(socket.recv(BufferSize).decode(Encoding))
        except Exception:
            print('=' * 5, Name, 'has disconnected from the server', '=' * 5, '\n')
            break


        with open('group_7.json', 'r') as File:

            jason_results = json.loads(File.read())
            records_results = Functions.send_records(socket, option, jason_results)
            if records_results == 'quit':
                print('=' * 5, Name, 'has disconnected from the server', '=' * 5, '\n')
                break
            else:
                print('=' * 5, 'request received from', Name, '=' * 5, '\n')













with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress)  # Creating the server socket and assigning IP address and port number
    Server_socket.listen()

    while True:
        socket_A, Address = Server_socket.accept()


        thread1 = threading.Thread(target=connection, args=(socket_A, Address))
        thread1.start()
























