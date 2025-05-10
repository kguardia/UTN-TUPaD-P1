"""
Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
"""

# Creamos la lista "animales"
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos el segundo valor (índice = 1) por "loro"
animales[1] = "loro"

# Reemplazamos el último valor (índice = 3) por "loro"
animales[3] = "oso"

# Imprimimos la lista resultante
print(animales)

# Otra manera es utilizar indexing con números negativos
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
# Reemplazamos el último valor (índice = -1) por "loro"
animales[-1] = "oso"

print(animales)