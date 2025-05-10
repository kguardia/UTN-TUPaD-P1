"""
Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""
# Creamos la lista "autos"
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos el índice 1
autos[1] = "etios"

# Reemplazamos el índice 2
autos[2] = "hilux"

# Imprimimos la lista resultante
print(autos)

# Otra forma: como los índices son consecutivos, podemos reemplazar ambos a la vez
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos los índices 1 y 2 a la vez
autos[1:3] = ["etios", "hilux"]

print(autos)