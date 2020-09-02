#!/usr/bin/python3
import getopt, os, random, string, sys, time
import multiprocessing as mp


def get_opts():
    try:
        (opts, args) = getopt.getopt (sys.argv[1:], "n:f:r:", [])
        return opts
    except getopt.GetoptError as err:
        print("Error: " + str(err))
        exit()


def run_process(r, lock, file):
    letter = random.choice(string.ascii_letters)
    run_file = open(file, "a")
    lock.acquire()
    for i in range(int(r)):
        time.sleep(1)
        run_file.write(letter)
        run_file.flush()
        print("Process:", os.getpid(), "letter:", letter)
    lock.release()
    run_file.close()


def main():
    if len(sys.argv[1:]) > 1:
        proc = 0
        file = ""
        iterations = 0
        opts = get_opts()
        for (opt, arg) in opts:
            if opt == "-n":
                proc = int(arg)
            if opt == "-f":
                file = arg
            if opt == "-r":
                iterations = int(arg)
        lock = mp.Lock()
        for i in range(proc):
            p = mp.Process(target=run_process, args=(iterations, lock, file))
            p.start()

        for i in range(proc):
            p.join()

    else:
        print("Try again")


if __name__ == "__main__":
    main()
