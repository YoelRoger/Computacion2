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