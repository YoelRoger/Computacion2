#!/usr/bin/python
import sys
import getopt


def main():
    # ver si esta correctamente cargado los parametros

    try:
        (opt, args) = getopt.getopt(sys.argv[1:], 'm:n:o:', [])
    except getopt.GetoptError as warning:
        print("ERROR: no respeto la carga de opciones y argumentos", str(warning))
        exit()
    # ver si son 3 argumentos y opciones

    if len(opt) != 3:
        print("no se ingreso la cantidad de parametros y argumentos correctos")
        exit()
    else:
        print("OPCIONES INGRESADAS: ", opt)

    num1 = "0"
    num2 = "0"

# checkeo de argumentos

    for (op, arg) in opt:
        if op == "-n":
            print("number 1:", arg)
            num1 = arg
        elif op == "-m":
            print("number 2:", arg)
            num2 = arg
        elif op == "-o":
            print("operacion:", arg)

        # ERRORES
        # ver si son enteros

        if op == "-n":
            try:
                num1 = int(arg)
            except ValueError:
                print("numero 1 introducido no es entero")
                print("Numero: ", arg)
                exit()
        if op == "-m":
            try:
                num2 = int(arg)
            except ValueError:
                print("numero 2 introducido no es entero")
                print("Numero: ", arg)
                exit()
        # ver si se ingreso operaciones validas
        if op == "-o":
            if arg not in ["+", "-", "x", "/"]:
                print("NO INGRESO UNA OPERACION VALIDA [ + - / x]")
                exit()
        # calculamos

        if op == "-o":
            if arg == "+":
                print(num1, "+", num2, "=", num1 + num2)
            elif arg == "-":
                print(num1, "-", num2, "=", num1 - num2)
            elif arg == "x":
                print(num1, "x", num2, "=", num1 * num2)
            elif arg == "/":
                try:
                    print(num1, "/", num2, "=", num1 / num2)
                except ZeroDivisionError as warning:
                    print("No es posible division por 0", warning)
                    sys.exit()
                    # division * 0 Error


main()

