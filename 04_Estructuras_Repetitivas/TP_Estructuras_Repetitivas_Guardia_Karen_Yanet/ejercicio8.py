"""
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

# Cantidad de números a ingresar
CANTIDAD = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    
    # Verifica si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verifica si es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Resultados
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")