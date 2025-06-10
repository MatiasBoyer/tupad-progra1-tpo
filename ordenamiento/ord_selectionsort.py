import time, random

def selection_sort(lista):
    # Empiezo desde el índice X
    for x in range(len(lista)):
        # Busco el elemento más pequeño desde X hasta el final, dando una posición Y
        for y in range(x + 1, len(lista)):
            if lista[y] < lista[x]:
                # En caso de que el elemento Y sea menor al elemento X, los intercambio
                lista[x], lista[y] = lista[y], lista[x]
    # Repito sumando 1 a X (for loop)

    return lista

lista = [random.randint(1, 100) for x in range(10000)]
print(f"La lista desordenada tiene {len(lista)} elementos")
print(f"Los primeros 10 elementos son: {lista[:10]}")

tiempo_inicial = time.time()
lista_ordenada = selection_sort(lista)
tiempo_final = time.time()
print(f"La lista ordenada tiene {len(lista_ordenada)} elementos")
print(f"Los primeros 10 elementos son: {lista_ordenada[:10]}")
print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicial:.6f} segundos")

