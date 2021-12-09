import socket
import requests
BufferSize = 4096
Encoding = 'ascii'
import time

limit = 5

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

            socket.send(str(records["arrival"]["terminal"]).encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["arrival"]["gate"]).encode(Encoding))
            time.sleep(0.01)
        print('  records sent\n')

    elif option == 2:


        print('  List of delayed flights')

        for records in json_response['data']:
            socket.sendall(records["flight"]["iata"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["departure"]["airport"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["departure"]["actual"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["arrival"]["estimated"].encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["departure"]["terminal"]).encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["departure"]["gate"]).encode(Encoding))
            time.sleep(0.01)
        print('  records sent\n')


    elif option == 3:

        for records in json_response['data']:
            socket.sendall(records["flight"]["iata"].encode(Encoding))
            time.sleep(0.01)

            socket.send(records["departure"]["airport"].encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["departure"]["actual"]).encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["arrival"]["estimated"]).encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["departure"]["terminal"]).encode(Encoding))
            time.sleep(0.01)

            socket.send(str(records["departure"]["gate"]).encode(Encoding))
            time.sleep(0.01)
        print('  records sent\n')








def receiving_records (socket):

    i = 1
    stop_point = 0
    while stop_point<limit:
        flight_code = socket.recv(BufferSize)
        airport = socket.recv(BufferSize)
        arrival = socket.recv(BufferSize)
        terminal = socket.recv(BufferSize)
        gate = socket.recv(BufferSize)
        if not flight_code:
            break

        print('='*15, 'flight', i, '='*15)

        print('  flight code:',flight_code.decode(Encoding),
              '\n  airport:',airport.decode(Encoding),
              '\n  arrival time:',arrival.decode(Encoding),
              '\n  terminal:',terminal.decode(Encoding),
              '\n  gate:',gate.decode(Encoding))
        i+=1
        stop_point+=1




def recv_flights(socket):

    i =1
    stop_point =0
    while stop_point<limit:
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
              '\n  arrival time:',arrival,
              '\n  terminal:', terminal,
              '\n  gate:', gate)
        i += 1
        stop_point+=1















