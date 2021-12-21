import socket
import json
import Functions

ServerAddress = ('127.0.0.1', 60060)
BufferSize = 4096
Encoding = 'ascii'

# creating the client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Client_socket:

    # connecting to the server
    try:
        Client_socket.connect(ServerAddress)
    except Exception:

        # if their is an error connecting to the server the program will print error massage and end the program
        print('\n', '=' * 15, "Can not connect to the server", '=' * 15, '\n')
        exit()
    print('=' * 15, 'Client is ready', '=' * 15, '\n\n')

    # ask the user to enter the username and send it to the server
    Name = input('User Name: ')

    Client_socket.send(Name.encode(Encoding))

    # check for API request errors
    error_check = Client_socket.recv(BufferSize).decode(Encoding)
    if error_check == 'Error':
        print('\n request error')
        exit()

    # ask the user to select an option
    print("Option List",
          '\n  1. Arrived flights. ',
          '\n  2. Delayed flights.',
          '\n  3. All flights coming from a specific city.',
          '\n  4. Details of a particular flight.',
          '\n  5. Quit.\n')

    # a while loop accept the user request until the user decide to quit
    while True:

        try:
            option = int(input('\nSelect an option =>'))
        except Exception:
            print('incorrect input')
            continue

        Client_socket.send(str(option).encode(Encoding))

        if option == 1:
            Functions.receiving_records(Client_socket)

        elif option == 2:
            Functions.recv_flights(Client_socket)

        elif option == 3:
            city = input('Enter the city name: ')
            Client_socket.send(city.encode(Encoding))

            Functions.recv_flights(Client_socket)

        elif option == 4:
            icao = input('Enter the flight icao: ')
            Client_socket.send(icao.encode(Encoding))

            Functions.flight_details(Client_socket)



        elif option == 3:
            city = input('Enter the city name: ')
            Client_socket.send(city.encode(Encoding))

            Functions.recv_flights(Client_socket)

        else:
            break




















