import socket
import json
import Functions

ServerAddress = ('127.0.0.1', 60060) 
BufferSize = 4096
Encoding = 'ascii'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as Client_socket:
    try:
        Client_socket.connect(ServerAddress)
        print('='*15,'Client is ready','='*15,'\n\n')
    except:
        print('='*15,'Failed to connect to the server ','='*15,'\n\n')

    Name = input('User Name: ')

    Client_socket.send(Name.encode(Encoding))

    print("Option List",
          '\n  1. Arrived flights. ',
          '\n  2. Delayed flights.',
          '\n  3. All flights coming from a specific city.',
          '\n  4. Details of a particular flight.\n')

    while True:

        option = int(input('Select an option =>'))
        Client_socket.send(str(option).encode(Encoding))

        if option == 1:
            Functions.receiving_records(Client_socket)

        elif option == 2:
           Functions.recv_delay()

        else:
          break


            


















    

