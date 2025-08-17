"""2. Utilizar el concepto de módulo necesariamente. Y Escribir un programa
para el manejo de listas el cuál cumplirá los siguientes requerimientos (2
ptos):
Reglas:
- Crear una función que le permitirá almacenar X números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función. X solo
puede ser entero. No otro tipo de dato. Y también un índice existente en la
lista.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es el mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo"""


import random

# Función 1: Genera una lista con X números aleatorios
def generar_lista(cantidad):
    if not isinstance(cantidad, int):
        print("La cantidad debe ser un número entero.")
        return []

    lista = []
    for _ in range(cantidad):
        numero = random.randint(1, 100)
        lista.append(numero)

    print("Lista generada:", lista)
    return lista

# Función 2: Filtra los números que no están repetidos
def obtener_no_repetidos(lista):
    no_repetidos = []
    for numero in lista:
        if lista.count(numero) == 1:
            no_repetidos.append(numero)

    print("Números no repetidos:", no_repetidos)
    return no_repetidos

# Función 3: Ordena de mayor a menor y menor a mayor
def ordenar_lista(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)

    print("Mayor a menor:", mayor_a_menor)
    print("Menor a mayor:", menor_a_mayor)

    return mayor_a_menor, menor_a_mayor

# Función 4: Encuentra el número par más grande
def mayor_par(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)

    if not pares:
        print("No hay números pares.")
        return None

    mayor = max(pares)
    print("Mayor número par:", mayor)
    return mayor
