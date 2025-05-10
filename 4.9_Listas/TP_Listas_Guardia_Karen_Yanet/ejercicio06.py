"""
Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""
#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} X {i} = {numero*i}")

num=int(input("ingrese un numero: "))
tabla_multiplicar(num)