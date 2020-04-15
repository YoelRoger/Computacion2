#!/usr/bin/python
from os import fork, getpid, getppid
from sys import argv
from getopt import getopt


def main():
    (opts, args) = getopt(argv[1:], "n:")  # el viejo y confiabele getopt+arg
    numChild = 0
    for (opt, arg) in opts:  # Lectura opciones
        if opt == '-n':
            numChild = int(arg)
            print(numChild)
    for x in range(numChild):  # Da a luz
        createChld = fork()
        if createChld == 0:
            talk()


def talk():  # imprimo consinga
    idprocceschld = getpid()
    idfather = getppid()
    print("soy el proceso", idprocceschld, "y mi padre es", idfather)
    exit()


main()
