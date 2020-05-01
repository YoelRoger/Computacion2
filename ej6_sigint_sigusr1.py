#!/usr/bin/python
import time
import os
import signal


def handler_hijo(sig, frame):
    print("señal SIGUSR1 recibida de padre PID %d" % os.getppid())


def handler_padre(sig, frame):
    print("ADIEU, FINALIZANDO")
    signal.signal(signal.SIGINT, signal.SIG_DFL)


def main():
    pid = os.fork()

    if pid:

        signal.signal(signal.SIGINT, handler_padre)
        for i in range(10):
            time.sleep(10)
            os.kill(pid, signal.SIGUSR1)
        print("PADRE ASESINANDO HIJO")
        os.kill(pid, signal.SIGTERM)
    else:

        signal.signal(signal.SIGUSR1, handler_hijo)
        while True:
            signal.pause()


main()

