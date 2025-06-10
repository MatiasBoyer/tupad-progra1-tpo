import time

def busqueda_binaria(valor_a_buscar, lista):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor_a_buscar:
            return medio
        elif lista[medio] < valor_a_buscar:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("La lista ordenada es:", lista)

valor = int(input("Ingrese el valor a buscar: "))

tiempo_inicial = time.time()
posicion = busqueda_binaria(valor, lista)
tiempo_final = time.time()
print(f"El valor {valor} se encuentra en la posición {posicion}")
print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicial:.6f} segundos")

