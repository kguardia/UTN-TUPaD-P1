"""
Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""

import math
def calcular_area_circulo(radio):
    area=math.pi*radio**2.0
    return area
def calcular_perimetro_circulo(radio):
    perimetro=2*math.pi*radio
    return perimetro

r=int(input("Ingrese el radio: "))
print(calcular_area_circulo(r))
print(calcular_perimetro_circulo(r))
