"""
Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
"""

def segundos_a_horas(segundos):
    horas=0
    horas=segundos/3600
    print(f"La cantidad de horas son: {horas}")

segundos= int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)