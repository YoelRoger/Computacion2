import socket, getopt
from sys import argv


def getOp():
    try:
        (opts, args) = getopt.getopt(argv[1:], 'p:t:f', [])
        return opts
    except getopt.GetoptError as error:
        print("COULD'T SUCCEED ERROR:", str(error))
        exit()
