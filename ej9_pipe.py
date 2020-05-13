import os
from os import wait, pipe, fork, getpid, getppid
from time import sleep
import signal


def handlerUSR2_A(signal, frame):
    print("Proceso A (PID=%d) leyendo:\n" % getpid())


def handlerUSR1_B(signal, frame):
    print("Mensaje 1 (PID=%d)\n" % getpid())


def handlerUSR1_C(signal, frame):
    print("Mensaje 2 (PID=%d)\n" % getpid())


def main():
    r, w = pipe()
    child = fork()

    if not child:
        signal.signal(signal.SIGUSR1, handlerUSR1_B)
        ppid = getppid()
        signal.pause()

        os.close(r)
        gc = fork()
        if not gc:
            # PROCESO C ESCRIBE
            signal.signal(signal.SIGUSR1, handlerUSR1_C)
            signal.pause()

            message = "Mensaje 2 (PID=" + str(getpid()) + ")\n"

            with os.fdopen(w, 'w') as w:
                w.write(message)
                w.close()

            sleep(2)
            os.kill(ppid, signal.SIGUSR2)

            exit(0)
        else:
            # PROCESO B ESCRIBE
            message = "Mensaje 1 (PID=" + str(getpid()) + ")\n"
            with open(w, 'w') as w:
                w.write(message)
                w.flush()

            sleep(2)
            os.kill(gc, signal.SIGUSR1)

    else:
        signal.signal(signal.SIGUSR2, handlerUSR2_A)
        sleep(2)
        os.kill(child, signal.SIGUSR1)
        signal.pause()

    # PROCESO A LEE
        os.close(w)
        with open(r, 'r') as r:
            while True:
                line = r.readline()
                if line:
                    print(line)
                else:
                    break
            r.close()

        wait()
        exit(0)


if __name__ == '__main__':
    main()
