"""Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos."""

from datetime import datetime

def mostrar_hora(func):
    def wrapper(*args, **kwargs):
        ahora = datetime.now()
        hora = ahora.hour
        minuto = ahora.minute
        print(f"El decorador está siendo ejecutado a las {hora}h con {minuto} minutos")


        resultado = func(*args, **kwargs)

        return resultado
    return wrapper


@mostrar_hora
def procesar_numeros(*args, **kwargs):

    suma_args = sum(args) if args else 0


    suma_kwargs = sum(kwargs.values()) if kwargs else 0


    suma_total = suma_args + suma_kwargs


    todos_numeros = list(args) + list(kwargs.values())
    if todos_numeros:
        mayor = max(todos_numeros)
    else:
        mayor = None

    print(f"Suma total de los números: {suma_total}")
    if mayor is not None:
        print(f"El número mayor es: {mayor}")
    else:
        print("No se ingresaron números.")
    return suma_total, mayor



# Ejemplo 1:
print("\nEjemplo 1:")
procesar_numeros(10, 5, 23, 4, 12, 8)

# Ejemplo 2:
print("\nEjemplo 2:")
procesar_numeros(a=7, b=15, c=3, d=20, e=11, f=6)

# Ejemplo 3:
print("\nEjemplo 3:")
procesar_numeros(5, 9, 14, x=22, y=17, z=3)


