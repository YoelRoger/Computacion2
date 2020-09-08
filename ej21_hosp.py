#!/usr/bin/python3

import multiprocessing
import time
import random
import getopt
import sys


def leaving(consult, patients, lock, salir_min, salir_max):
    while True:
        time.sleep(random.randint(salir_min, salir_max))
        lock.acquire()
        patients.value = patients.value - 1
        lock.release()
        consult.release()
        print("Paciente atendido... Quedan:", consult.get_value(), "consultorios disponibles.... Paciente:", int(patients.value))


def joining(consult, patients, lock, entrar_min, entrar_max):
    while True:
        consult.acquire()
        time.sleep(random.randint(entrar_min, entrar_max))
        lock.acquire()
        patients.value = patients.value + 1
        lock.release()
        print("Paciente entrando. Quedan", consult.get_value(), "consultorios disponibles. Paciente:", int(patients.value))


if __name__ == "__main__":
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'z:a:b:c:d:', ["consultorios", "entrar_min", "entrar_max", "salir_min", "salir_max"])

        num_consultorios = 5
        entrar_min = 1
        entrar_max = 3
        salir_min = 5
        salir_max = 7

        for arg in opts:
            if arg[0] == "-z":
                num_consultorios = arg[1]
            elif arg[0] == "-a":
                entrar_min = arg[1]
            elif arg[0] == "-b":
                entrar_max = arg[1]
            elif arg[0] == "-c":
                salir_min = arg[1]
            elif arg[0] == "-d":
                salir_max = arg[1]
            else:
                print("Wrong parameters try [ ./ej21_hosp.py -z 5 -b 3 -c 5 d 7")
                exit(1)

        patients = multiprocessing.Value('d', 0)

        lock = multiprocessing.Lock()

        consult = multiprocessing.Semaphore(num_consultorios)

        multiprocessing.Process(target=joining, args=(consult, patients, lock, entrar_min, entrar_max,)).start()
        multiprocessing.Process(target=leaving, args=(consult, patients, lock, salir_min, salir_max,)).start()

    except Exception as e:
        print("Error:", e)
