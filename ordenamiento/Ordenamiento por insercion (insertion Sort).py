import time
import random

# Función de ordenamiento por inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual
    return arr

# //////////////////////////////////
# Lista pequeña
lista_pequeña = [10, 2, 8, 6, 7, 5, 3, 9, 1, 4]
print("Lista pequeña original:", lista_pequeña)

inicio_peq = time.time()
ordenada_pequeña = insertion_sort(lista_pequeña.copy())
fin_peq = time.time()

print("Lista pequeña ordenada:", ordenada_pequeña)
print("⏱️ Tiempo lista pequeña:", round(fin_peq - inicio_peq, 6), "segundos")

#////////////////////////////////////////////
# Lista grande (1000 elementos aleatorios)
lista_grande = random.sample(range(1, 1001), 1000)
print("\nLista grande generada con 1000 elementos")

inicio_gra = time.time()
ordenada_grande = insertion_sort(lista_grande.copy())
fin_gra = time.time()

print("⏱️ Tiempo lista grande:", round(fin_gra - inicio_gra, 6), "segundos")