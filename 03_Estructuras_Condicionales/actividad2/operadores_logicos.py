EDAD_MINIMA = 21

edad = int(input("Ingrese su edad: "))
categoria = input("Ingrese su categoría (A, B, C, D, E, F, G): ")

if edad >= EDAD_MINIMA and (categoria == "D" or categoria == "d"):
    print("Puede conducir ambulancias.")
else:
    print("No puede conducir ambulancias.")