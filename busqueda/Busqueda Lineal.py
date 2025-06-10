import time

# Creamos la "biblioteca" con libros del 1 al 1.000.000
biblioteca = list(range(1, 1000001))  # lista de 1 a 1.000.000

# Libro que queremos encontrar
objetivo = 50

# Funcion de busqueda lineal
def busqueda_lineal(lista, objetivo):
    for indice, libro in enumerate(lista):
        if libro == objetivo:
            return indice  # posicion donde lo encontro
    return -1  # si no lo encuentra

# tiempo de busqueda
inicio_tiempo = time.time()
resultado = busqueda_lineal(biblioteca, objetivo)
fin_tiempo = time.time()

# Mostramos resultados
if resultado != -1:
    print(f"📘 Libro encontrado en la posición {resultado}")
else:
    print("❌ Libro no encontrado.")

print(f"⏱ Tiempo de búsqueda lineal: {fin_tiempo - inicio_tiempo:.6f} segundos")
