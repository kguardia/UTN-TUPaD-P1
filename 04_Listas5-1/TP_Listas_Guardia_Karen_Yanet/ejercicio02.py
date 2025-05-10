"""
Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
"""

# Creamos una lista con 5 elementos cualesquiera
sabores_de_helado = ["vainilla", "chocolate", "pistacho", "frutilla a la crema", "cookies and cream"]

# Imprimimos el penúltimo elemento, que será el que se encuentre en el índice número 3
print(sabores_de_helado[3])

# Otra manera es utilizar indexing con números negativos
sabores_de_helado = ["vainilla", "chocolate", "pistacho", "frutilla a la crema", "cookies and cream"]

# -1 imprimiría el último elemento, entonces -2 imprimirá el penúltimo
print(sabores_de_helado[-2])
