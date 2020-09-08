#!/usr/bin/python3

import multiprocessing, getopt, sys, socket


def process(lock, client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        exit_client = False
        try:
            if command == "ABRIR":
                client_socket.send("Ingrese archivo /ruta :".encode())
                name_file = client_socket.recv(1024).decode()
                client_socket.send("Ingrese 'CERRAR', 'AGREGAR' o 'LEER'".encode())
                while True:
                    command = client_socket.recv(1024).decode()
                    print("RECIBIDO", command)
                    if command == "CERRAR":
                        client_socket.send("CONEXION/ARCHIVO CERRADO".encode())
                        exit_client = True
                        break
                    elif command == "AGREGAR":
                        file = open(name_file, "a")
                        client_socket.send("Ingrese Texto".encode())
                        text = client_socket.recv(1024).decode()
                        text = text + "    "
                        lock.acquire()
                        file.write(text)
                        file.close()
                        lock.release()
                        client_socket.send("Agregado correctamente".encode())
                    elif command == "LEER":
                        client_socket.send(open(name_file, "r").read().encode())
                    else:
                        client_socket.send("Ingrese otro comando [AGREGAR, CERRAR, LEER] ".encode())
            else:
                client_socket.send("Debe abrir un archivo [use ABRIR]".encode())
        except Exception as error:
            client_socket.send("Error: ".encode() + str(error).encode())
        if exit_client:
            break


if __name__ == "__main__":
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:', ["puerto"])

        port = 8000

        for arg in opts:
            if arg[0] == "-p":
                port = int(arg[1])
            else:
                print("Ingrese parametros correctos [ej ./ej20_sock_lock -p 6000]")
                exit(1)

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        serversocket.bind((host, port))
        serversocket.listen(5)
        print("SERVER LISTENING ...")
        lock = multiprocessing.Lock()
        while True:
            clientsocket, adress = serversocket.accept()
            child = multiprocessing.Process(target=process, args=(lock, clientsocket,))
            child.start()

    except Exception as error:
        print("Error:", error)







