"""
Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
"""
# Importar las librerías
import random
from statistics import mean, median, mode

# Crear la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los valores estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar los valores
print("Lista de números aleatorios:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Comparar y determinar el sesgo
# Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir "Sesgo positivo o a la derecha"
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
# Si la media es menor que la mediana y la mediana es menor que la moda, imprimir "Sesgo negativo o a la izquierda"
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
# Si la media, la mediana y la moda son iguales, imprimir "Sin sesgo"
elif media == mediana == moda:
    print("Sin sesgo")
# Si no se cumple ninguna de las condiciones anteriores, imprimir "No se puede determinar si esta distribución tiene sesgo o no"
else:
    print("No se puede determinar si esta distribución tiene sesgo o no")