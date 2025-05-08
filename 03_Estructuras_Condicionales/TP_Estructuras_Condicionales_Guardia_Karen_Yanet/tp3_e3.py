"""
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
"""
# Solicitar un número par al usuario
num = int(input("Ingrese un número: "))

# Verificar si es un número par usando el operador %
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")