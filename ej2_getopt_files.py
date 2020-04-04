#!/usr/bin/python
import sys
import getopt


def main():

    try:
        (opt, args) = getopt.getopt(sys.argv[1:], 'i:o:', [])
    except getopt.GetoptError as warning:
        print("ERROR: no respeto la carga de opciones y argumentos", str(warning))
        exit()

    if len(opt) != 2:  # tambien podria ser mas especifico con un < y >
        print("no se ingreso la cantidad de parametros y argumentos correctos")
        exit()
    else:
        print("OPCIONES INGRESADAS:>>>>>> ", opt)
    # defino archivo a copiar y a crear o reemplazar
    for op, arg in opt:
        if op == '-i':
            infile = arg
        else:
            pastefile = arg
    try:
        FileIn = open(infile, "r")
    except FileNotFoundError as error:
        print("ARCHIVO A COPIAR NO ENCONTRADO!")
        print(error)
        exit()
        return

    lines = FileIn.readlines()
    FileIn.close()

    FilePaste = open(pastefile, "w")
    FilePaste.writelines(lines)
    FilePaste.close()

    print("HECHO")


main()
