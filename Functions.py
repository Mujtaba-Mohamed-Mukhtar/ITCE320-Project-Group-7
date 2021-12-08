import socket
import requests
BufferSize = 4096
Encoding = 'ascii'

def send_records (socket, option, json_response):

    if option == 1:

        print(' List of  all arrived flights')

        for records in json_response['data']:

            print('sending records')

            socket.sendall(records["flight"]["iata"].encode(Encoding))
            socket.send(records["departure"]["airport"].encode(Encoding))
            socket.send(records["arrival"]["actual"].encode(Encoding))
            socket.send(records["arrival"]["terminal"].encode(Encoding))
            socket.send(str(records["arrival"]["gate"]).encode(Encoding))

        print('records sent\n')



def receiving_records (socket):

    while True:
        flight_code = socket.recv(BufferSize)
        airport = socket.recv(BufferSize)
        arrival = socket.recv(BufferSize)
        terminal = socket.recv(BufferSize)
        gate = socket.recv(BufferSize)
        if not flight_code or not arrival or not airport:
            break

        print('flight code:',flight_code.decode(Encoding),
              '\nairport:',airport.decode(Encoding),
              '\narrival time:',arrival.decode(Encoding),
              '\nterminal:',terminal.decode(Encoding),
              '\ngate:',gate.decode(Encoding))















