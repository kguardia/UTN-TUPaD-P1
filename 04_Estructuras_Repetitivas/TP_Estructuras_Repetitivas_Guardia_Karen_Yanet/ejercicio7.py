"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
"""
# Solicitar al usuario un número entero positivo: 
limite = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if limite > 0:
    suma = 0
    for numero in range(0,limite+1):
        suma += numero
    print(f"La suma de los números de 0 a {limite} es de {suma}.")
else:
    print("El número ingresado no es positivo.")