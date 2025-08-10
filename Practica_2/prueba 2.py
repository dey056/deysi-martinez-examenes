"""- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""

def normalizar_nombres(nombres):

    nombres_normalizados = []


    for nombre in nombres:

        nombre_limpio = nombre.strip().title()


        partes = nombre_limpio.split()


        for parte in partes:
            if parte not in nombres_normalizados:
                nombres_normalizados.append(parte)


    return nombres_normalizados

# Ejemplo:
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
