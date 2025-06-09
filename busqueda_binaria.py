import time
import random

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

tamaño_lista = 1000000
lista = random.sample(range(1, 1000000000), tamaño_lista)
lista = sorted(lista) # Obtenemos una lista ordenada
objetivo = random.choice(lista)

inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(lista, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:} segundos")