EDAD_MINIMA = 18
cant_personas = int(input("Ingrese una cantidad de personas: "))
cant_personas_mayores = 0

for cont in range(cant_personas):
    print("Ingrese la edad n°",(cont+1))
    edad = int(input())
    if edad >= EDAD_MINIMA:
        cant_personas_mayores += 1

porc = (cant_personas_mayores / cant_personas) * 100
print(f"El porcentaje de personas mayores de edad es: {porc}.")