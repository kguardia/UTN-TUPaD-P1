"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
"""

# Programa para sumar números ingresados por el usuario hasta que ingrese 0
total = 0 #Inicializamos una variable acumuladora

print("Ingresa números enteros para sumarlos. Ingresa 0 para finalizar.")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:  # Condición para detener el bucle
        break
    total += numero  # Sumar el número al total acumulado

print(f"El total acumulado es: {total}")
