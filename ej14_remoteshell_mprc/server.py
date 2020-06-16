import subprocess, socket, getopt, sys, multiprocessing


def child(clientsocket, addr):

    while True:
        data = clientsocket.recv(1024)
        if data.decode('ascii') == 'exit':
            clientsocket.send('FINISHED'.encode('ascii'))
            break
        print("ADDRESS: %s " % str(addr))
        print("\nRECEIVED CORRECTLY: " + data.decode("ascii"))
        result = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = result.communicate()
        if stdout != "":
            msg = "OK\n"+stdout
        elif stderr != "":
            msg = "ERROR\n"+stderr

        clientsocket.send(msg.encode())

def main():
    (option, value) = getopt.getopt(sys.argv[1:], "l")
    for (opt, arg) in option:
        if opt == "-l":
            port = arg
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8000
    s.bind((host, port))
    s.listen(5)
    print("SERVER LISTENING...")
    while True:
        clientsocket, addr = s.accept()

        client = multiprocessing.Process(target=child, args=(clientsocket, addr))

        client.start()


main()
