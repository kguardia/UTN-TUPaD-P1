"""
Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
"""

for cont in range(100,-1,-1):
    if cont % 2 == 0:
        print(cont)