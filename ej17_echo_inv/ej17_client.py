#!/usr/bin/python
import socket, getopt
from sys import argv, exit, stdin


def getOp():
    try:
        (opts, args) = getopt.getopt(argv[1:], 'p:h:', [])
        return opts
    except getopt.GetoptError as error:
        print("COULD'T SUCCEED ERROR:", str(error))
        exit()


def socketStructure(host, port):
    host = host
    port = port

    try:
        socketCreated = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("FAILED TO CREATE SOCKET")
    exit()
    socketCreated.connect((host, port))
    while True:
        try:
            msgin = input('ENTER MESSAGE ....>>>>>> ')
            socketCreated.send(msgin.encode('assci'))
        except EOFError:
            break


def main():
    options = getOp()
    for (opts, args) in options:
        if opts == '-p':
            port = int(args)
        if opts == '-h':
            host = args
    socketStructure(host, port)


main()
