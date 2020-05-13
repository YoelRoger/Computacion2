#!/usr/bin/python
import signal
import time
import os
import sys
import getopt


def handlerUSR2(signal, frame):
    print("Soy el PID>> ", os.getpid(), "recibí la señal>> ", signal, "de mi padre PID>>", os.getppid())


def main():
    (opts, args) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

    if len(opts) != 1:
        print("no se ingreso la cantidad de parametros y argumentos correctos")
        exit()

    for opt, value in opts:
        if opt == "-p" or opt == "--process":
            num_chld = int(value)

            # CANT HIJOS
            for x in range(num_chld):
                pid1 = os.fork()
                # PADRE
                if pid1:
                    time.sleep(1)
                    print("Creando proceso: ", pid1, "\n\n")
                    send_signal(pid1)
                    os.wait()
                    print("TERMINA2")
                # HIJO
                else:
                    signal.signal(signal.SIGUSR2, handlerUSR2)
                    signal.pause()
                    exit(0)


def send_signal(pid):
    pid = int(pid)
    os.kill(pid, signal.SIGUSR2)


if __name__ == '__main__':
    main()
