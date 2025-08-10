"""- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

def procesar_notas(estudiantes):
    # Diccionario de resultados
    resultados = {}

    # Variables
    mejor_promedio_nombre = ""
    mejor_promedio_valor = -1

    # Notas de cada estudiante
    for nombre, notas in estudiantes.items():

        promedio = (notas[0] + notas[1] + notas[2]) / 3


        if promedio >= 11:
            estado = "aprobado"
        else:
            estado = "desaprobado"


        resultados[nombre] = {
            "promedio": promedio,
            "estado": estado
        }


        if promedio > mejor_promedio_valor:
            mejor_promedio_valor = promedio
            mejor_promedio_nombre = nombre


    print("Estudiante con mayor promedio:", mejor_promedio_nombre)
    print("Promedio:", mejor_promedio_valor)


    return resultados

# Estudiantes
estudiantes = {
    "Miguel": [12, 14, 15],
    "Antonio": [10, 9, 8],
    "Efrain": [13, 14, 13]
}

resultados = procesar_notas(estudiantes)
print(resultados)
