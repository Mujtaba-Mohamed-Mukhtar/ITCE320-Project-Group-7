# packages used in the program
import requests
import json
import socket
import threading
import Functions

ServerAddress = ('127.0.0.1', 60060)  # Server IP address and port number
BufferSize = 4096  # Number of bit the client and the server can receive
Encoding = 'ascii'  # the algorithm used to encrypt and decrypt the packets

print('=' * 15, 'Server is ready', '=' * 15, '\n\n')


def connection(socket, address):
    # this function is going to receive clients requests and process them and send the required records

    # receiving the client name
    Name = socket.recv(BufferSize).decode(Encoding)
    print('=' * 5, Name, 'is connected', '=' * 5, '\n')

    # assigning the api request parameters
    params = {
        'access_key': '843591f5114e7c7994823d002e7b6013',
        'limit': 100
    }

    # creating .json file to save the retrieved records
    with open('group_7.json', 'w') as file:

        # getting the flights records from aviationstack.com and storing them in the file
        api_response = requests.get('http://api.aviationstack.com/v1/flights', params)

        # check if their is an error in the request
        if api_response.status_code != 200:
            print('!' * 5, 'Request error')
            socket.send('Error'.encode(Encoding))
        socket.send('no error'.encode(Encoding))

        json.dump(api_response.json(), file, indent=3)

    option = 0

    while True:

        # receiving the option the client selected and passing it to send_records function to retrieve the requested records
        try:
            option = int(socket.recv(BufferSize).decode(Encoding))
        except Exception:
            print('=' * 5, Name, 'has disconnected from the server', '=' * 5, '\n')
            break

        # reading the retrieved record stored in the file
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
    Server_socket.listen()  # waiting for client connection

    # using while loop to accept multiple client connection
    while True:
        socket_A, Address = Server_socket.accept()

        # creating a thread to handle clients requests and passing the name of the function to it
        thread1 = threading.Thread(target=connection, args=(socket_A, Address))
        thread1.start()
