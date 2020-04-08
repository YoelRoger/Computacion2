#!/usr/bin/python
import sys
import getopt
import subprocess
import datetime

def main():

    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'c:f:l', [])
    except getopt.GetoptError as warning:
        print("ERROR: no respeto la carga de opciones y argumentos", str(warning))
        exit()

    if len(opts) != 3:
        print("no se ingreso la cantidad de parametros y argumentos correctos")
        exit()

    command = ""
    out_file = ""
    log_file = ""
    for opt, arg in opts:
        if opt == '-c':
            command = arg
        elif opt == '-f':
            out_file = open(arg, "a")
        else:
            log_file = open(arg, "a")
    process = subprocess.Popen([command], stdout=out_file, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    error = process.communicate()[1]

    if not error:
        log_file.write(str(datetime.datetime.now()) + " Comando " + command + " ejecutado correctamente")
        out_file.write("\n")
    else:
        log_file.write(str(datetime.datetime.now()) + ">>" + str(error))
    out_file.close()
    log_file.close()


main()
