import socket, getopt
from sys import argv, exit, stdin


def getOp():
    try:
        (opts, args) = getopt.getopt(argv[1:], 'a:t:p', [])
        return opts
    except getopt.GetoptError as error:
        print("COULD'T SUCCEED ERROR:", str(error))
        exit()


def socketStructure(host, port, protocol):
    host = host
    protocol = protocol
    port = port
    if protocol == 'tcp' or protocol == 'TPC':
        print("TCP PROTOCOL ENTERED")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("FAILED TO CREATE SOCKET")
        exit()
        s.connect((host, port))
        while True:
            try:
                msgin = input('ENTER MESSAGE ...: ')
                s.send(msgin.encode('assci'))
                if msgin == 'exit' or msgin == 'EXIT':
                    s.close()
                    break
            except EOFError:
                break
    elif protocol == 'udp' or protocol == 'UDP':
        print("UDP PROTOCOL SELECTED")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error:
            print('FAILED TO CREATE SOCKET')
            exit()
        while True:
            msgin = input("ENTER MESSAGE...:").encode()
            s.sendto(msgin, (host, port))
            if msgin.decode() == 'exit':
                s.close()
                break
    else:
        print("PROTOCOL NOT RECOGNISED PLEASE ENTER 'UDP' OR 'TCP'")


def main():
    options = getOp()
    for (opts, args) in options:
        if opts == '-p':
            port = int(args)
        if opts == '-t':
            protocol = args
        if opts == '-a':
            host = args
    socketStructure(host, port, protocol)


main()
