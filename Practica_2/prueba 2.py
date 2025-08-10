def normalizar_nombres(nombres):

    nombres_normalizados = []


    for nombre in nombres:

        nombre_limpio = nombre.strip().title()


        partes = nombre_limpio.split()


        for parte in partes:
            if parte not in nombres_normalizados:
                nombres_normalizados.append(parte)


    return nombres_normalizados

# Ejemplo de uso:
lista_original = [
    "  julian  ",
    "sofia",
    "LIZ diaz",
    "miguel",
    "emilia",
    "JULIAN",

]

resultado = normalizar_nombres(lista_original)

print("Lista original:", lista_original)
print("Nombres normalizados:", resultado)
