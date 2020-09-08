import socket, getopt
from sys import argv


def main():
    def get_op():
        try:
            (opts, args) = getopt.getopt(argv[1:], 'p:t:f', [])
            return opts
        except getopt.GetoptError as error:
            print("COULD'T SUCCEED ERROR:", str(error))
            exit()

    options = get_op()
    for (opts, arg) in options:
        if opts == '-p':
            port = int(arg)
        if opts == '-t':
            protocol = arg
        if opts == '-f':
            pathfile = arg


    def socket_structure(port, protocol, pathfile):
        port = port
        protocol = protocol
        file = pathfile

        if protocol == 'tcp' or protocol == 'TCP':
            print('TCP PROTOCOL SELECTED')
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = ""
            serversocket.bind((host, port))
            serversocket.listen(5)
            print('SERVER LISTENING ...')
            clientsocket, addr = serversocket.accept()

            while True:
                f = open(file, "a")
                d = clientsocket.recv(1024)
                f.write(d.decode("ascii") + '\n')
                if d == "" or len(d) == 0:
                    print('Exiting...')
                    break
                print("Address: %s " % str(addr))
                print("Received correctly: " + d.decode("ascii"))


        elif protocol == 'udp' or protocol == 'UDP':
            print('UDP PROTOCOL SELECTED')
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host = ""
            serversocket.bind((host, port))
            print('SERVER LISTENING ...')

            while True:
                f = open(file, "a")
                d, addr = serversocket.recvfrom(1024)
                f.write(d.decode("ascii") + '\n')
                address = addr[0]
                port = addr[1]

                if d == "" or len(d) == 0:
                    print('Exiting...')
                    break
                print("Address: %s - Port %d" % (address, port))
                print("Received correctly: " + d.decode("ascii"))

        else:
            print("PROTOCOL NOT RECOGNISED PLEASE ENTER 'UDP' OR 'TCP'")

    socket_structure(port, protocol, pathfile)

 main()

