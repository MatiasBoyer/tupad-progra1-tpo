import time, random

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]

    return quick_sort(izquierda) + centro + quick_sort(derecha)

lista = [random.randint(1, 100) for x in range(10000)]
print(f"La lista desordenada tiene {len(lista)} elementos")
print(f"Los primeros 10 elementos son: {lista[:10]}")

tiempo_inicial = time.time()
lista_ordenada = quick_sort(lista)
tiempo_final = time.time()
print(f"La lista ordenada tiene {len(lista_ordenada)} elementos")
print(f"Los primeros 10 elementos son: {lista_ordenada[:10]}")
print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicial:.6f} segundos")

