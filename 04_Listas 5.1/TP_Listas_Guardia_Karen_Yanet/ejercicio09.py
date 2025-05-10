
"""
Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla

"""
# Creamos la lista "compras"
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agregamos "jugo" a la lista del tercer cliente (compras[2])
compras[2].append("jugo")

# Reemplazamos "fideos" por "tallarines" en la lista del segundo cliente (compras[1])
compras[1][1] = "tallarines"

# Eliminamos "pan" de la lista del primer cliente (compras[0])
compras[0].remove("pan")

# Imprimimos la lista resultante
print(compras)