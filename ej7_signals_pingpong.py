#!/usr/bin/python
import time
import os
import signal


def handler_chld2(signal, frame):
    print("Soy el hijo2 con PID:", os.getpid(), "\nPONG")


def handler_USR1(signal, frame):
    pass


def send_signal(pid):
    os.kill(pid, signal.SIGUSR1)


def main():
    signal.signal(signal.SIGUSR1, handler_USR1)

    pid1 = os.fork()

    if pid1:
        # PADRE
        pid2 = os.fork()
        if pid2:
            while True:
                signal.pause()
                send_signal(pid2)
                 # HIJO 2
        else:
            signal.signal(signal.SIGUSR1, handler_chld2)
            while True:
                signal.pause()
    else:
        # HIJO 1
        for i in range(10):
            print("\n")
            ppid = os.getppid()
            send_signal(ppid)
            print("Soy el hijo1 con PID:", os.getpid(), "\nPING")
            time.sleep(5)
        print("TERMINANDO.")
        os.kill(pid1, signal.SIGTERM)


if __name__ == '__main__':
    main()
