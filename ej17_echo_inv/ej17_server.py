#!/usr/bin/python
import getopt
import socket
from sys import argv


def main():

    port = None

    def get_op():
        try:
            (opts, args) = getopt.getopt(argv[1:], 'p:', [])
            return opts
        except getopt.GetoptError as error:
            print("COULD'T SUCCEED :C ERROR>>>", str(error))
            exit()

    options = get_op()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)

    def invert_msg(cadena):
        return cadena[::-1]

    def socket_structure(selected_port):
        selected_port = selected_port

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        serversocket.bind((host, selected_port))
        serversocket.listen(5)
        print('SERVER LISTENING ...')
        clientsocket, addr = serversocket.accept()

        while True:
            d = clientsocket.recv(1024)
            recived = (d.decode("ascii"))
            msg_reversed = invert_msg(recived)
            serversocket.send(msg_reversed.encode('assci'))
            print("Address: %s " % str(addr))
            print("Received correctly: " + d.decode("ascii"))

    socket_structure(port)


if __name__ == '__main__':
    main()
