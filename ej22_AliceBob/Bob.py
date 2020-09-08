import socket
from termcolor import colored

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 5000
server_socket.connect((host, port))


def bob_mind(socket):
    server_socket = socket
    bob_msg = ""
    while bob_msg != "cambio" and bob_msg != "exit":
        bob_msg = input("> ")
        server_socket.send(bob_msg.encode())
    if bob_msg == "cambio":
        alice_msg = ""
        while alice_msg != "cambio" and alice_msg != "exit":
            alice_msg = server_socket.recv(1024).decode()
            print(alice_msg)
        if alice_msg == "cambio":
            pass
        elif alice_msg == "exit":
                exit()
                print(colored("ALICE TEMRINA!", 'magenta'))
    elif bob_msg == "exit":
        server_socket.send("exit".encode())
        print(colored("BOB TERMINA2", 'red'))
        exit()


while True:
    try:
        bob_mind(server_socket)
    except Exception as error:
        print(error)

