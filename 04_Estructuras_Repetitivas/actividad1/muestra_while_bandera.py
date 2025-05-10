umbral = 10
sumatoria = 0
cont = 0

while sumatoria < umbral:
    cont += 1
    print("Ingrese número", cont)
    num = int(input())
    sumatoria += num
print(f"El promedio de valores es {(sumatoria / cont)}.")