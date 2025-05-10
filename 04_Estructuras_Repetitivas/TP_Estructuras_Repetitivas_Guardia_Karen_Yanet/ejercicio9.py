"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
"""
# Cantidad de números a ingresar
CANTIDAD = 100

# Inicializa la suma total
suma = 0

# Bucle para ingresar los números y sumarlos
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    suma += numero

# Calcula la media
media = suma / CANTIDAD

# Muestra el resultado
print(f"La media de los {CANTIDAD} números ingresados es: {media}.")