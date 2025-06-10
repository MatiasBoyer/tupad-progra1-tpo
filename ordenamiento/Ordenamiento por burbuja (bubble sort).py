import time
import random

# Función Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ////////////////////////////////
#  Lista pequeña
lista_pequeña = [10, 2, 8, 6, 7, 5, 3, 9, 1, 4]
print("Lista pequeña original:", lista_pequeña)

inicio_peq = time.time()
ordenada_pequeña = bubble_sort(lista_pequeña.copy())
fin_peq = time.time()

print("Lista pequeña ordenada:", ordenada_pequeña)
print("⏱️ Tiempo lista pequeña:", round(fin_peq - inicio_peq, 6), "segundos")

# ////////////////////////////////////////////////////////
# Lista grande (1000 elementos aleatorios)
lista_grande = random.sample(range(1, 1001), 1000)
print("\nLista grande generada con 1000 elementos (no se imprime ya que es muy grande)")

inicio_gra = time.time()
ordenada_grande = bubble_sort(lista_grande.copy())
fin_gra = time.time()

print("⏱️ Tiempo lista grande:", round(fin_gra - inicio_gra, 6), "segundos")