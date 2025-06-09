import time

# Inicialización de la tabla hash: una lista de "ranuras" (slots)
tamanio_tabla = 1000000
tabla_hash = [None] * tamanio_tabla

def insertar(tabla, clave, valor):
    indice = hash(clave) % len(tabla)
    if tabla[indice] is None:
        tabla[indice] = []  # Se utiliza una lista para manejar colisiones
    tabla[indice].append((clave, valor)) # Se almacena en la ranura como una tupla (clave, valor)

def buscar(tabla, clave):
    indice = hash(clave) % len(tabla)
    if tabla[indice] is not None:
        for (k, v) in tabla[indice]:
            if k == clave:
                return v
    return None  # No se encontró el elemento

# Ejemplo de uso:
insertar(tabla_hash, "manzana", 150)
insertar(tabla_hash, "banana", 120)
print(buscar(tabla_hash, "banana"))  # Devuelve 120

# Medicion de tiempo:
inicio = time.time()
insertar(tabla_hash, "pera", 200)
resultado = buscar(tabla_hash, "pera")
fin = time.time()
tiempo = fin - inicio

print(f"Búsqueda hash: Resultado = {resultado}, Tiempo = {tiempo} segundos")