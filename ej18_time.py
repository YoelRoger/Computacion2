import socket, getopt
from sys import argv, exit


def main():
    protocol = ""
    host = ""
    port = 0
    (options, args) = getopt.getopt(argv[1:], 'h:t:p:', [])

    for (opts, args) in options:
        if opts == '-p':
            port = int(args)
        if opts == '-t':
            protocol = args
        if opts == '-h':
            host = args

    if protocol == "tcp" or protocol == "TPC":
        print("TCP PROTOCOL SELECTED")
        try:
            socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("FAILED TO CREATE SOCKET", socket.error)
            exit()

    elif protocol == "udp" or protocol == "UDP":
        print("UDP PROTOCOL SELECTED")
        try:
            socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print("FAILED TO CREATE SOCKET", socket.error)
            exit()
    else:
        print("PROTOCOL NOT RECOGNISED PLEASE ENTER 'UDP' OR 'TCP'")

    socket_client.connect((host, port))
    msg = socket_client.recv(1024)

    print("mensaje del servidor", msg.decode())


main()

