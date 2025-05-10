"""
Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
"""
# Programa para sumar números entre dos valores excluyéndolos
valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))

# Determinar los límites en orden ascendente usando loops
if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2
else:
    inicio = valor2 + 1
    fin = valor1

# Calcular la suma usando un bucle
suma = 0
for numero in range(inicio, fin):
    suma += numero
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")
