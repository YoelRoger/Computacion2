#!/usr/bin/python
import socket, getopt
from sys import argv


def main():
    port = None
    host = None

    def get_opt():
        try:
            (opts, args) = getopt.getopt(argv[1:], 'p:h:', [])
            return opts
        except getopt.GetoptError as error:
            print("COULD'T SUCCEED ERROR:", str(error))

    options = get_opt()
    for (opts, args) in options:
        if opts == '-p':
            port = int(args)
        if opts == '-h':
            host = args

    def socket_structure(host, port):
        host = host
        port = port

        try:
            socket_created = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("FAILED TO CREATE SOCKET")

        socket_created.connect((host, port))
        while True:
            try:
                msgout = input('ENTER MESSAGE ....>>>>>> ')
                socket_created.send(msgout.encode())
                msgin = socket_created.recv(1024)
                print("SERVER SAY>>>"+msgin.decode())
            except EOFError:
                break

    socket_structure(host, port)


if __name__ == '__main__':
    main()
