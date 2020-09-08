#!/usr/bin/python3

import socket, getopt, sys

if __name__ == "__main__":

    (opts, args) = getopt.getopt(sys.argv[1:], 'p:', ["puerto"])

    for arg in opts:
        if arg[0] == "-p":
            port = int(arg[1])
        else:
            print("Ingrese parametros correctos [ej ./ej20_sock_lock -p 6000]")
            exit(1)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    server_socket.connect((host, port))
    while True:
        try:
            msg = input(">>>>>>>> :").encode()
            server_socket.send(msg)
            request = server_socket.recv(1024).decode()
            print(request)
            if request == "CONEXION/ARCHIVO CERRADO":
                break
        except Exception as error:
            print(error)

