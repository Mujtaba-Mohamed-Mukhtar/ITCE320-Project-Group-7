import requests
import json
import socket
import threading
import time
import Functions

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

print('=' * 15, 'Server is ready', '=' * 15, '\n\n')


def connection(socket, address):
    Name = socket.recv(BufferSize).decode(Encoding)

    print('=' * 5, Name, 'is connected', '=' * 5, '\n')




    option = int(socket.recv(BufferSize).decode(Encoding))

    with open('group_7.json','w') as file:

        parameters = {}
        access_key = '6c8e01ffa60812094c287f7e6a3fd765'
        limit = 5

        if option == 1:
            parameters = {
                'access_key':access_key,
                'limit': limit,
                'flight_status':'landed'
            }
        elif option == 2:
            parameters = {
                'access_key': access_key,
                'min_delay_arr': 1,
                'limit': limit
            }
        elif option == 3:
            city_name = socket.recv(BufferSize).decode(Encoding)

            city_parameters = {
                'access_key': access_key,
                'city_name': city_name,
                'limit': 1

            }

            city_api_response = requests.get('http://api.aviationstack.com/v1/cities', city_parameters)
            if city_api_response.status_code != 200:
                print('!' * 5, 'Request error')

            city_iata = city_api_response['data']['iata_code']

            parameters = {
                'access_key': access_key,
                'limit': limit,
                'dep_iata': city_iata}
        elif option == 4:
            flight_icao = socket.recv(BufferSize).decode(Encoding)
            parameters = {
                'access_key': access_key,
                'limit': limit,
                'flight_icao': flight_icao

            }

        api_response = requests.get('http://api.aviationstack.com/v1/flights',parameters)

        if api_response.status_code != 200:
            print('!' * 5, 'Request error')




        json.dump(api_response.json(), file, indent=3)

    with open('group_7.json', 'r') as File:
        x = json.loads(File.read())

        Functions.send_records(socket,option,x)













with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress)  # Creating the server socket and assigning IP address and port number
    Server_socket.listen()
    socket_A, Address = Server_socket.accept()

    thread1 = threading.Thread(target=connection, args=(socket_A, Address))
    thread1.start()
