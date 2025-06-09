import time
import random


def bubble_sort(lista):
    ordered_list = list(lista)
    n = len(ordered_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ordered_list[j] > ordered_list[j + 1]:
                ordered_list[j], ordered_list[j + 1] = ordered_list[j + 1], ordered_list[j]
    return ordered_list


def selection_sort(lista):

    ordered_list = list(lista)
    n = len(ordered_list)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if ordered_list[j] < ordered_list[min_idx]:
                min_idx = j
        ordered_list[i], ordered_list[min_idx] = ordered_list[min_idx], ordered_list[i]
    return ordered_list


def insertion_sort(lista):

    ordered_list = list(lista)
    n = len(ordered_list) 

    for i in range(1, n):

        key = ordered_list[i]
        j = i - 1

        while j >= 0 and key < ordered_list[j]:
            ordered_list[j + 1] = ordered_list[j]
            j -= 1
        ordered_list[j + 1] = key

    return ordered_list


def quick_sort(lista):

    n = len(lista) 

    if n <= 1:
        return lista
    else:
        pivot = lista[n // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left_half = lista[:mid]
    right_half = lista[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result



def generate_random_list(size):
    return [random.randint(0, size * 10) for _ in range(size)]

def measure_and_sort(sort_function, original_arr):
    start_time = time.perf_counter()

    sorted_arr = sort_function(original_arr)
    end_time = time.perf_counter()
    return sorted_arr, end_time - start_time



if __name__ == "__main__":

    short_list_size = 500
    long_list_size = 100000


    short_list_original = generate_random_list(short_list_size)
    long_list_original = generate_random_list(long_list_size)

    sorting_algorithms = {
        "Burbuja": bubble_sort,
        "Selección": selection_sort,
        "Inserción": insertion_sort,
        "Rápido": quick_sort,
        "Mezcla": merge_sort
    }


    print("--- Resultados para la Lista Corta ---")
    print(f"Tamaño de la lista: {short_list_size}")
    print(f"Lista Original: {short_list_original}")
    print("-" * 30)

    for name, func in sorting_algorithms.items():
        sorted_list, time_taken = measure_and_sort(func, short_list_original)
        print(f"  Algoritmo: {name}")
        print(f"    Lista Ordenada: {sorted_list}")
        print(f"    Tiempo: {time_taken:.6f} segundos")
        print("-" * 30)

 
    print("\n--- Resultados para la Lista Larga ---")
    print(f"Tamaño de la lista: {long_list_size}")
    print(f"Lista Original (primeros 10 y últimos 10 elementos): {long_list_original[:10]} ... {long_list_original[-10:]}")
    print("-" * 30)

    for name, func in sorting_algorithms.items():
        sorted_list, time_taken = measure_and_sort(func, long_list_original)
        print(f"  Algoritmo: {name}")
        print(f"    Lista Ordenada (primeros 10 y últimos 10 elementos): {sorted_list[:10]} ... {sorted_list[-10:]}")
        print(f"    Tiempo: {time_taken:.6f} segundos")
        print("-" * 30)