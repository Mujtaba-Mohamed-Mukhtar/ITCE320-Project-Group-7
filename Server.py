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


    parameters = {}

    access_key = '3c20cacdeae406247164d1992c2a9fd4'
    limit = 5

    with open('group_7.json','w') as file:

        option = 0


        while True:

            try:
                option = int(socket.recv(BufferSize).decode(Encoding))
            except Exception:
                print('=' * 5, Name, 'has disconnected from the server', '=' * 5, '\n')
                break

            if option == 1:
                parameters = {
                    'access_key': access_key,
                    'limit': limit,
                    'flight_status': 'landed'
                }


            elif option == 2:
                parameters = {
                    'access_key': access_key,
                    'limit': limit,
                    'min_delay_arr': 1
                    }

            elif option == 3:
                country_name = socket.recv(BufferSize).decode(Encoding)

                country_parameters = {
                    'access_key': access_key,
                    'limit':1
                }
                city_api_response = requests.get('http://api.aviationstack.com/v1/airlines', country_parameters)
                if city_api_response.status_code != 200:
                    print('!' * 5, 'Request error')

                json_result = city_api_response.json()

                country_airline = ' '

                for name in json_result['data']:
                    if name["country_name"] == country_name:
                        country_airline = name["airline_name"]

                parameters = {
                    'access_key': access_key,
                    'limit': limit,
                    'airline_name':country_airline
                    }

            elif option == 4:
                flight_icao = socket.recv(BufferSize).decode(Encoding)
                parameters = {
                    'access_key': access_key,
                    'limit': 1,
                    'flight_icao': flight_icao
                }

            else:
                print('=' * 5, Name, 'has disconnected from the server', '=' * 5, '\n')
                break

            api_response = requests.get('http://api.aviationstack.com/v1/flights', parameters)

            if api_response.status_code != 200:
                print('!' * 5, 'Request error')

            json.dump(api_response.json(), file, indent=3)

            file.close()

            with open('group_7.json', 'r') as File:
                jason_results = json.loads(File.read())
                File.close()

            print('=' * 5, 'request received from', Name, '=' * 5, '\n')

            Functions.send_records(socket, option, jason_results)













with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind(ServerAddress)  # Creating the server socket and assigning IP address and port number
    Server_socket.listen()

    while True:
        socket_A, Address = Server_socket.accept()


        thread1 = threading.Thread(target=connection, args=(socket_A, Address))
        thread1.start()
























