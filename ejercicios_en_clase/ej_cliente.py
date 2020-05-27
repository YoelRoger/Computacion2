#!/usr/bin/python3
import sys
import socket
# CLIENTE PARA SERVIDOR TCP

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('FAILED TO CREATE SOCKET')
    sys.exit()

# set host
host = '167.71.159.138'
port = 8000

s.connect((host, port))
print("CONNECTED")

while True:

    msgin = input('ENTER NAME : ').encode()
    try:
        # enviar mensaje str
        msg = 'hello|' + msgin
        s.send(msg.encode('ascii'))

        # recibir data  (data, addr)
        respuesta = s.recv(1024)

        print('RESPUESTA DEL SV : ' + respuesta.decode("ascii"))

    except socket.error:
        print('CODIGO DE ERROR> : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    msgin = input('ENTER EMAIL : ').encode()
    try:
        # enviar mensaje str
        msg = 'email|' + msgin
        s.send(msg.encode('ascii'))

        # recibir data  (data, addr)
        respuesta = s.recv(1024)

        print('RESPUESTA DEL SV : ' + respuesta.decode("ascii"))

    except socket.error:
        print('CODIGO DE ERROR> : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    msgin = input('ENTER KEY : ').encode()
    try:
        # enviar mensaje str
        msg = 'key|' + msgin
        s.send(msg.encode('ascii'))

        # recibir data  (data, addr)
        respuesta = s.recv(1024)

        print('RESPUESTA DEL SV : ' + respuesta.decode("ascii"))

    except socket.error:
        print('CODIGO DE ERROR> : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    msg = 'exit'
    try:
        print("SENDING EXIT")
        s.send(msg)
        respuesta = s.recv(1024)

        print('RESPUESTA DEL SV: ' + respuesta.decode("ascii"))
        sys.exit()
    except socket.error:
        print('CODIGO DE ERROR> ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
s.close()
