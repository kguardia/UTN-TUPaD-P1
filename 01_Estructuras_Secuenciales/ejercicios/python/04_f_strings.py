nombre = input("Ingrese su nombre: ")
edad = input(f"Ingrese su edad, {nombre}: ")

saludo = f"Hola {nombre}, ¿Cómo estás?"
# Otras maneras de hacerlo poco prácticas
print("Tu nombre es",nombre,"y tu edad es", edad)
print("Tu nombre es " + nombre + " y tu edad es " + str(edad))
# Manera óptima de concatenar, con una sintaxis más agradable
print(f"Tu nombre es {nombre} y tu edad es {edad}")
print(saludo)
