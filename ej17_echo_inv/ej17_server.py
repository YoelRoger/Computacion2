#!/usr/bin/python
import socket, getopt
from sys import argv


def main():

    def getOp():
        try:
            (opts, args) = getopt.getopt(argv[1:], 'p:', [])
            return opts
        except getopt.GetoptError as error:
            print("COULD'T SUCCEED :C ERROR>>>", str(error))
            exit()

    options = getOp()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)

    def invertMsg(cadena):
        return cadena[::-1]

    def socketStructure(port):
        port = port

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        serversocket.bind((host, port))
        serversocket.listen(5)
        print('SERVER LISTENING ...')
        clientsocket, addr = serversocket.accept()

        while True:
            d = clientsocket.recv(1024)
            recived = (d.decode("ascii"))
            msgReversed = invertMsg(recived)
            serversocket.send(msgReversed.encode('assci'))
            print("Address: %s " % str(addr))
            print("Received correctly: " + d.decode("ascii"))

    socketStructure(port)


if __name__ == '__main__':
    main()

