#!/usr/bin/python
import os


def main():
    pipeOutput = '/tmp/msm'
    lines = ""
    fifo_file = open(pipeOutput, 'r')  # abro fifo para usar "pipe" pal msm
    msg = fifo_file.read()
    fifo_file.close()

    r, w = os.pipe()
    child = os.fork()

    if child:
        # PADRE
        os.close(r)
        write_file = os.fdopen(w, 'w')  # arch escribe en "pipe"
        write_file.write(msg)
        write_file.flush()
        write_file.close()

    else:
        os.close(w)
        read_file = os.fdopen(r, 'r')  # arch lee del "pipe"
        msm = read_file.read()
        if not msg:
            print("no se ingreso mensaje en producer")
        else:
            print("msm recibido del padre obtenido del fifo:" + msm)
        exit(0)


if __name__ == '__main__':
    main()
