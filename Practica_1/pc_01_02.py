"""Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes."""

matematicas = 17
ciencia = 14
historia = 15
prom_matematicas = 40*matematicas/100
prom_ciencia = 30*ciencia/100
prom_historia = 30*historia/100
nota_final_ponderada = prom_matematicas + prom_ciencia + prom_historia

print(("La nota final es: {}".format(f"{nota_final_ponderada:.1f}")))

if nota_final_ponderada >= 13.0:
    print("¿Aprobado?: Si")

print("El estudiante obtuvo una nota final de 15.5 y su estado final es: Aprobado")
