"""
Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""

def operaciones_basicas(a, b):
    suma= a+b
    resta= a-b
    div= a/b
    multi= a*b
    print(f"La suma de los numeros ingresados es: {suma}")
    print(f"La resta de los numeros ingresados es: {resta}")
    print(f"La division de los numeros ingresados es: {div}")
    print(f"La multiplicacion de los numeros ingresados es: {multi}")



a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
operaciones_basicas(a,b)