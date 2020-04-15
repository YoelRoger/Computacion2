#!/usr/bin/python
from os import getpid, wait, fork


def main():
    child = fork()
    # print('QUE GUARDA CHILD STRT', child)
    if child:
        # PADRE
        idprocess = getpid()
        # print('esto guarda ip', idprocess)
        print('soy el padre, PID:', idprocess, 'mi hijo es', child)
        print('soy el padre, PID:', idprocess, 'mi hijo es', child)
        wait()  # ESPERO A HIJO
        print('Mi porceso hijo, PID:', child, 'termino')
    else:
        # HIJO
        imp5timesChild()
        print('hijo PID:', getpid(), 'terminado')

        # print('ESTO GUARDA CHILD PA HIJO', child)
        exit()


def imp5timesChild():
    for x in range(5):
        print('soy el hijo, PID:', getpid())
    return


main()
