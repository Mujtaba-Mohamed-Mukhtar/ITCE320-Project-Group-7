'''
this program script contain all the function used to send and receive the data between the
client and the server, it also contain function to check for errors in retrieving and sending records
'''



import socket
import requests
BufferSize = 4096
Encoding = 'ascii'
import time

access_key = '843591f5114e7c7994823d002e7b6013'
limit = 100


def send_records (socket, option, json_response):

    if option == 1:

        # this option select all the arrived flights records and send them to the client
        print('  List of  all arrived flights')

        No_records = True

        for records in json_response['data']:

            if records["flight_status"] == "landed":

                No_records = False

                socket.send(records["flight"]["iata"].encode(Encoding))
                time.sleep(0.01)

                try:
                    socket.send(str(records["departure"]["airport"]).encode(Encoding))
                    time.sleep(0.01)
                except Exception:
                    socket.send(str(records["arrival"]["airport"]).encode(Encoding))
                    time.sleep(0.01)

                socket.send(records["arrival"]["actual"].encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["terminal"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["gate"]).encode(Encoding))
                time.sleep(0.01)
        print('  records sent\n')
        if No_records:
            socket.send('no records'.encode(Encoding))
        else:
            socket.send('STOP'.encode(Encoding))

    elif option == 2:

        # this option select all the delayed flights records and send them to the client
        print('  List of delayed flights')

        No_records = True

        for records in json_response['data']:

            if records["arrival"]["delay"] is not None:
                No_records = False

                socket.sendall(records["flight"]["iata"].encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["departure"]["airport"]).encode(Encoding))
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
        if No_records:
            socket.send('no records'.encode(Encoding))
        else:
            socket.send('STOP'.encode(Encoding))

    elif option == 3:

        '''this option receive a city name from the client and select all the flights records 
        arriving from that city and send them to the client'''
        country_name = socket.recv(BufferSize).decode(Encoding)

        print('  All flights arriving from', country_name)

        country_parameters = {
            'access_key': access_key,
            'limit': limit
        }
        city_api_response = requests.get('http://api.aviationstack.com/v1/airports', country_parameters)
        if city_api_response.status_code != 200:
            print('!' * 5, 'Request error')
            return

        json_result = city_api_response.json()

        country_iata_code = ' '

        for name in json_result['data']:
            if name["country_name"] == country_name.title():
                country_iata_code = str(name["iata_code"])
                break

        No_records = True

        for records in json_response['data']:

            if records["departure"]["iata"] == country_iata_code:
                No_records = False

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
        if No_records:
            socket.send('no records'.encode(Encoding))
        else:
            socket.send('STOP'.encode(Encoding))

    elif option == 4:

        '''this option receive a flight icao code from the client and select all the flights records 
                that have the same code and send them to the client'''
        flight_icao = socket.recv(BufferSize).decode(Encoding)
        No_records = True

        for records in json_response['data']:
            if records["flight"]["icao"]:
                No_records = False

                socket.sendall(records["flight"]["iata"].encode(Encoding))
                time.sleep(0.01)

                socket.sendall(records["flight_date"].encode(Encoding))
                time.sleep(0.01)

                socket.send(records["departure"]["airport"].encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["departure"]["gate"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["departure"]["terminal"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["airport"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["terminal"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["gate"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["flight_status"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["departure"]["scheduled"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["scheduled"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["estimated"]).encode(Encoding))
                time.sleep(0.01)

                socket.send(str(records["arrival"]["delay"]).encode(Encoding))
                time.sleep(0.01)
        print('  records sent\n')
        if No_records:
            socket.send('no records'.encode(Encoding))
        else:
            socket.send('STOP'.encode(Encoding))

    # if the client select other option the program will print quit massage and end the connection
    else:
        return 'quit'









def receiving_records (socket):

    i = 1

    while True:
        flight_code = socket.recv(BufferSize).decode(Encoding)
        if flight_code == 'no records':
            print('== No arrived flight')
            break
        elif flight_code == 'STOP':
            break
        airport = socket.recv(BufferSize)
        arrival = socket.recv(BufferSize)
        terminal = socket.recv(BufferSize)
        gate = socket.recv(BufferSize)




        print('='*15, 'flight', i, '='*15)

        print('  flight code:',flight_code,
              '\n  airport:',airport.decode(Encoding),
              '\n  arrival time:',arrival.decode(Encoding),
              '\n  terminal:',terminal.decode(Encoding),
              '\n  gate:',gate.decode(Encoding))
        i+=1




def recv_flights(socket):

    i =1
    while True:
        flight_code = socket.recv(BufferSize).decode(Encoding)
        if flight_code == 'no records':
            print('\n== No flight records')
            break
        elif flight_code == 'STOP':
            break

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
              '\n  gate:', gate,'\n')
        i += 1



def flight_details(socket):

    while True:
        flight_code = socket.recv(BufferSize).decode(Encoding)
        if flight_code == 'no records':
            print('\n== No arrived flight')
            break
        elif flight_code == 'STOP':
            break

        date = socket.recv(BufferSize).decode(Encoding)

        departure_airport = socket.recv(BufferSize).decode(Encoding)

        departure_gate = socket.recv(BufferSize).decode(Encoding)

        departure_terminal = socket.recv(BufferSize).decode(Encoding)

        arrival_airport = socket.recv(BufferSize).decode(Encoding)

        arrival_terminal = socket.recv(BufferSize).decode(Encoding)

        arrival_gate = socket.recv(BufferSize).decode(Encoding)

        flight_status = socket.recv(BufferSize).decode(Encoding)

        scheduled_departure = socket.recv(BufferSize).decode(Encoding)

        scheduled_arrival = socket.recv(BufferSize).decode(Encoding)

        estimated_arrival = socket.recv(BufferSize).decode(Encoding)

        delay = socket.recv(BufferSize).decode(Encoding)

        print('=' * 15, 'flight', '=' * 15)
        print('  Flight code:', flight_code,
              '\n  Date:',date,
              '\n  Departure airport:', departure_airport,
              '\n  Departure gate:', departure_gate,
              '\n  Departure terminal:',departure_terminal,
              '\n  Arrival airport:', arrival_airport,
              '\n  Arrival terminal:', arrival_terminal,
              '\n  Arrival gate:', arrival_gate,
              '\n  Flight status:',flight_status,
              '\n  Scheduled departure:',scheduled_departure,
              '\n  Scheduled arrival:',scheduled_arrival,
              '\n  Estimated arrival:',estimated_arrival,
              '\n  Delay:',delay,'\n')














