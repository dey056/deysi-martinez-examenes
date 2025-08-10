"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente:
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""
nombre = "Deysi Martinez"
salario = 2500
edad = "29"
compañia = "CITEmadera"
potencia = salario ** 2
diez_por_ciento = 5*salario/100
bono_final = potencia + diez_por_ciento

print ("Tipos de variables:")
print ("El tipo de variable de tu nombre es:")
print(type(nombre))
print ("El tipo de variable de tu salario es:")
print(type(salario))
print ("El tipo de variable de tu edad es:")
print(type(edad))
print ("El tipo de variable de tu compañia es:")
print(type(compañia))

print("------------------------------------------------------")
print("Hola {}, por laborar en {}".format(nombre, compañia))

if int(edad) > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
if int(edad) < 30:
    print("Usted tiene un bono de 5% en el mes de diciembre")

print("El bono final para su salario de {} es de: {}".format(salario, bono_final))

