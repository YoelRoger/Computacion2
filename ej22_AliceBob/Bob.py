#!/usr/bin/python3
from time import sleep
import socket
from termcolor import colored

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 4000
server_socket.connect((host, port))


def send(server_socket):
    while True:
        bob_msg = input("Bob: ")
        if bob_msg == 'cambio' or bob_msg == 'CAMBIO':
            server_socket.send(bob_msg.encode())
            sleep(2)
            break
        if bob_msg == 'exit' or bob_msg == 'EXIT':
            server_socket.send(bob_msg.encode())
            print(colored("BOB TERMINA2", 'red'))
            exit()
        else:
            server_socket.send(bob_msg.encode())


def to_Receive(server_socket):
    while True:
        alice_msg = server_socket.recv(1024).decode()
        if alice_msg == 'cambio' or alice_msg == 'CAMBIO':
            print("Alice dice:", alice_msg)
            break
        if alice_msg == 'exit' or alice_msg == 'EXIT':
            print(colored("ALICE DIJO NOS MATEMOS!", 'magenta'))
            exit()
        else:
            print("Alice dice:", alice_msg)


while True:
    send(server_socket)
    to_Receive(server_socket)
