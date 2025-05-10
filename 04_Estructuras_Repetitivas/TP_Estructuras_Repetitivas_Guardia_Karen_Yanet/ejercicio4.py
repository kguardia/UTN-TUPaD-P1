"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""

# Incializar la suma acumulada y el número ingresado
suma = 0
numero = int(input("Ingresa un número entero (0 para terminar): "))

# Bucle para pedir números hasta que el usuario ingrese 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

# Mostrar la suma total
print(f"La suma total es: {suma}.")