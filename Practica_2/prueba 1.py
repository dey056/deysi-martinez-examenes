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
