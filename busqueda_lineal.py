import time
import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

tamaño_lista = 1000000
lista = random.sample(range(1, 1000000000), tamaño_lista)  # Lista de números únicos
objetivo = lista[tamaño_lista - 1] # El peor caso para la búsqueda lineal es cuando el objetivo está al final

inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(lista, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")