cant_numeros = 5
sumatoria = 0

for cont in range(1,cant_numeros+1):
    print("Ingrese número", cont)
    num = int(input())
    sumatoria += num
    print()
    
print(f"La sumatoria de los valores es {sumatoria}.")
print(f"El valor promedio es {(sumatoria / cant_numeros)}.")
