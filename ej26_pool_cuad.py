import multiprocessing as mp
import getopt, sys, os
from termcolor import cprint


def split_list(alist, wanted_parts):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts] for i in range(wanted_parts)]


def calculateSq(number):
    cprint(("Pool worker PID", os.getpid(), "calculating..."), "yellow")
    return number ** 2


def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'p:m:n:', [])
        return opts
    except getopt.GetoptError as error:
        cprint(('Error en Getopt: ' + str(error)), "red")
        exit()


opts = getOpts()

for (opt, arg) in opts:
    if opt == "-p":
        process = int(arg)
    elif opt == "-m":
        num_min = int(arg)
    elif opt == "-n":
        num_max = int(arg)


def main():
    pool = mp.Pool()
    list_range = list(range(num_min, num_max))
    splited_list = split_list(list_range, process)
    for values in splited_list:
        map_f = (pool.map(calculateSq, values))
        cprint(("These are the resulting squares:", map_f), "cyan")
    cprint("-------------------------------------", "yellow")
    for values in splited_list:
        apply_f = [pool.apply(calculateSq, args=(i,)) for i in values]
        cprint(("These are the resulting squares:", apply_f), "cyan")
    pool.close()


if __name__ == "__main__":
    main()
