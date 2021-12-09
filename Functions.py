import socket
import requests
BufferSize = 4096
Encoding = 'ascii'
import time

def send_records (socket, option, json_response):

    if option == 1:

        print('  List of  all arrived flights')

        for records in json_response['data']:
            socket.sendall(records["flight"]["iata"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["departure"]["airport"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["arrival"]["actual"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["arrival"]["terminal"].encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["arrival"]["gate"]).encode(Encoding))
            time.sleep(0.01)


        print('  records sent\n')
        socket.send('$T0P'.encode(Encoding))



def receiving_records (socket):

    i = 1
    while True:
        flight_code = socket.recv(BufferSize)
        airport = socket.recv(BufferSize)
        arrival = socket.recv(BufferSize)
        terminal = socket.recv(BufferSize)
        gate = socket.recv(BufferSize)
        if not flight_code or not arrival or not airport:
            break
        print('='*15, 'flight', i, '='*15)

        print('flight code:',flight_code.decode(Encoding),
              '\nairport:',airport.decode(Encoding),
              '\narrival time:',arrival.decode(Encoding),
              '\nterminal:',terminal.decode(Encoding),
              '\ngate:',gate.decode(Encoding))
        i+=1
        stop_point+=1
        
def recv_delay(socket):
    i=1
    stop_point = 0
    while stop_point < limit
        flight_code = socket.recv(BufferSize).decode(Encoding)
        airport = socket.recv(BufferSize).decode(Encoding)
        departure = socket.recv(BufferSize).decode(Encoding)
        arrival = socket.recv(BufferSize).decode(Encoding)
        terminal = socket.recv(BufferSize).decode(Encoding)
        gate = socket.recv(BufferSize).decode(Encoding)

        print('=' * 15, 'flight', i, '=' * 15)
        print('  flight code:', flight_code,
              '\n  airport:', airport,
              '\n  departure time:', departure,
              '\n  arrival time:', arrival,
              '\n  terminal:', terminal,
              '\n  gate:', gate)
        i += 1
        stop_point += 1
        















