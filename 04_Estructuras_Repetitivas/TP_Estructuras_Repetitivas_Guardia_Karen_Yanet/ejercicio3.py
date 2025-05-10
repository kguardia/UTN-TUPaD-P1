"""
Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
"""
# Solicitar al usuario dos números enteros
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Asegurar que el rango se recorra correctamente, sin importar el orden en que se ingresen los números
menor = min(inicio, fin)
mayor = max(inicio, fin)

# Sumar los números entre 'menor' y 'mayor', excluyéndolos
suma = 0
for numero in range(menor+1,mayor):
    suma += numero

# Mostrar el resultado
print(f"La suma de los números entre {menor} y {mayor} es: {suma}.")