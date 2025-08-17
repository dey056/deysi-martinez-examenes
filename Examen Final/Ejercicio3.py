"""Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante."""


from datetime import datetime

def conteo(func):
    def wrapper(*args, **kwargs):
        cantidad_parametros = len(args) + len(kwargs)
        if cantidad_parametros <= 1:
            print("La función necesita más de un parámetro para procesar la lógica.")
            return
        resultado = func(*args, **kwargs)
        print("La función fue ejecutada.")
        return resultado
    return wrapper

@conteo
def registrar_alumno(nombre, edad, hora, minuto, nota1, nota2, nota3, nota4):
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos")
    print(f"El promedio del estudiante es: {promedio}")

ahora = datetime.now()
hora_actual = ahora.hour
minuto_actual = ahora.minute

registrar_alumno("Deysi", 29, hora_actual, minuto_actual, 16, 17, 12, 19)



