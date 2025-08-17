"Continuacion de ejercicio 2"

from Ejercicio2 import (
    generar_lista,
    obtener_no_repetidos,
    ordenar_lista,
    mayor_par
)

# Llamamos a las funciones desde el módulo
lista = generar_lista(10)  # Cambia 10 por cualquier número entero

lista_no_repetidos = obtener_no_repetidos(lista)

orden_mayor, orden_menor = ordenar_lista(lista_no_repetidos)

mayor = mayor_par(lista_no_repetidos)
