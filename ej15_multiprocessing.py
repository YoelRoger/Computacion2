import sys, os, signal
import multiprocessing as mp


def STDIN_reader(r):
    print("Reading from STDIN, press Ctrl+D to exit")
    sys.stdin = open(0)
    while True:
        try:
            msg = input()
            r.send(msg)
        except EOFError:
            print("Exit")
            break


def PIPE_reader(w):

    while True:
        msg = w.recv()
        print('Reading (pid: %d): %s' % (os.getpid(), msg))


def main():
    a, b = mp.Pipe()
    proc1 = mp.Process(target=STDIN_reader, args=(a,))
    proc2 = mp.Process(target=PIPE_reader, args=(b,))
    proc1.start()
    proc2.start()
    proc1.join()
    os.kill(proc2.pid, signal.SIGTERM)


if __name__ == '__main__':
    main()