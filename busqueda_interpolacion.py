import time
import random

def busqueda_interpolacion(lista, objetivo):
    inicio, fin = 0, len(lista) - 1

    while inicio <= fin and lista[inicio] <= objetivo <= lista[fin]:
        
        pos = inicio + ((objetivo - lista[inicio]) * (fin - inicio) // (lista[fin] - lista[inicio])) # Calcular la posición estimada

        if lista[pos] == objetivo:
            return pos
        elif lista[pos] < objetivo:
            inicio = pos + 1
        else:
            fin = pos - 1

    return -1  # No encontrado


tamaño_lista = 1000000
lista = random.sample(range(1, 1000000000), tamaño_lista)
lista = sorted(lista) # Obtenemos una lista ordenada
objetivo = random.choice(lista)

inicio = time.time()
resultado = busqueda_interpolacion(lista, objetivo)
fin = time.time()
tiempo = fin - inicio

print(f"Búsqueda de interpolación: Resultado = {resultado}, Tiempo = {tiempo:.6f} segundos")