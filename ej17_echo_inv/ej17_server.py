#!/usr/bin/python3

import getopt
import socket
from sys import argv
import multiprocessing


def invert_message(client_socket, address):
    while True:
        data = client_socket.recv(1024)
        received = data.decode()
        if received == "":
            break
        msg_reversed = received[::-1]
        client_socket.send(msg_reversed.encode())
        print("Address: %s " % str(address), "Received correctly: " + data.decode())


def main():

    port = None

    (options, args) = getopt.getopt(argv[1:], 'p:', [])

    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('SERVER LISTENING ...')

    while True:
        client_socket, address = server_socket.accept()
        cliet = multiprocessing.Process(target=invert_message, args= (client_socket,address))
        cliet.start()


if __name__ == '__main__':
    main()
