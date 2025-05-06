def alumnos_trabajo ():
    print("----------")
    print(" Karen Guardia\n Agustina Grille\n Erika Gonzalez\n Nicolas Gonzalez")
    print("----------")


def binario(num):
    while True:
        try:
            valor = int(input(num))
            if valor in [0, 1]:
                return valor
            else:
                print("Por favor, ingrese solo 0 o 1")
        except ValueError:
            print("Error")


def menu():
    opcion=int(input("Valores numericos para las operaciones\n 1.AND\n 2.OR\n 3.NOT\n 4.NAND\n 5.NOR\n 6.XOR\n 7.Salir\n" \
    "Ingrese el valor numerico: "))
    return opcion


def puerta_logica():
    while True:
        lista = menu()
        if lista == 1 or lista ==2 or lista ==3 or lista ==4 or lista ==5 or lista ==6:
            a= binario("Ingrese el primer valor binario (0 o 1): ")
            b= binario("Ingrese el segundo valor binario (0 o 1): ")
            print("----------")
            if lista == 1:
                print(f"Resultado: {a} AND {b} = {a & b}")
                print("----------")
            elif lista == 2:
                print(f"Resultado: {a} OR {b} = {a | b}")
                print("----------")
            elif lista == 3:
                print(f"Resultado: {a} NOT = {int(not a)}")
                print(f"Resultado: {b} NOT = {int(not b)}")
                print("----------")
            elif lista == 4:
                print(f"Resultado: {a} NAND {b} = {int(not (a & b))}")
                print("----------")
            elif lista == 5:
                print(f"Resultado: {a} NOR {b} = {int(not (a | b))}")
                print("----------")
            elif lista == 6:
                print(f"Resultado: {a} XOR {b} = {a ^ b}")
                print("----------")
        elif lista == 7:
            print("----------")
            print("Gracias por usar el simulador de puertas")
            alumnos_trabajo()
            break
        else:
            print("Entrada no válida, por favor ingresar el número correspondiente")
            print("----------")


puerta_logica()
