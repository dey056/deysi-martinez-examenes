"""Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
Monto total con propina: S/. 230.00
Cada persona debe pagar: S/. 115.00
¡Advertencia! El monto por persona supera los S/. 100"""

#Entrada esperada:
cuenta = float(input("Total de la cuenta: "))
porcent_propina = float(input("Porcentaje de propina: "))
cantidad_personas = int(input("Número de personas: "))

monto_total_con_propina= cuenta * (1 + porcent_propina / 100)
monto_persona = monto_total_con_propina / cantidad_personas

print(f"Monto total con propina: S/. {monto_total_con_propina:.2f}")
print(f"Cada persona debe pagar: S/. {monto_persona:.2f}")

if monto_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")

