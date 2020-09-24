#!/usr/bin/python3
from time import sleep
from termcolor import colored
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 4000
server_socket.bind((host, port))
server_socket.listen(5)
print("WORKING AS SV")
client_socket, adress = server_socket.accept()


def send(client_socket):
    while True:
        alice_msg = input("Alice: ")
        if alice_msg == 'cambio' or alice_msg == 'CAMBIO':
            client_socket.send(alice_msg.encode())
            sleep(2)
            break
        if alice_msg == 'exit' or alice_msg == 'EXIT':
            client_socket.send(alice_msg.encode())
            print(colored("ALICE TEMRINA!", 'magenta'))
            exit()
        else:
            client_socket.send(alice_msg.encode())


def to_Receive(client_socket):
    while True:
        bob_msg = client_socket.recv(1024).decode()
        if bob_msg == 'cambio' or bob_msg == 'CAMBIO':
            print("Bob dice:", bob_msg)
            break
        if bob_msg == 'exit' or bob_msg == 'EXIT':
            print(colored("BOB DIJO NOS MATEMOS!", 'red'))
            exit()
        else:
            print("Bob dice:", bob_msg)


while True:
    to_Receive(client_socket)
    send(client_socket)
