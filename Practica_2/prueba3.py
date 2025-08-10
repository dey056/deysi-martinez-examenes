"""- Se requiere verificar una lista de números de diferentes países, el
área de soporte al cliente recibe diariamente ciento de números en
distintos formatos. Estos números pueden venir con o sin código,
espacios, guines, paréntesis, o hasta textos no válido

- Crear la función de normalizar_telefonos(numeros, pais_defecto) la
cual para sus parámetros tendrá las siguientes especificaciones:
numeros: lista con números telefónicos
pais_defecto: en caso no tenga un número un prefijo lo agrega de
acuerdo al país ( “PE”->”+51”, “AR”->”+54”, “CL”->”+56”)
Si el prefijo no existe entre los ya mencionados indicar un mensaje
que no es válido y que debe ingresar un prefijo válido
- Devolverá un dict con:
“válidos”: una lista de números con formato: +<código><numeroNacional>
“invalidos”: lista con los números o valores inválidos y al inicio de esa
lista agregar el valor de “NO VÁLIDOS”
- No mutará la lista de entrada original"""

def normalizar_telefonos(numeros, pais_defecto):

    codigos_pais = {
        "PE": "+51",
        "AR": "+54",
        "CL": "+56"
    }

    # Verificar si el país por defecto es válido
    if pais_defecto not in codigos_pais:
        print("Prefijo de país no válido. Debe ser 'PE', 'AR' o 'CL'.")
        return None

    prefijo = codigos_pais[pais_defecto]
    validos = []
    invalidos = ["NO VÁLIDOS"]

    for numero in numeros:

        numero_str = str(numero).strip()


        limpio = ""
        for c in numero_str:
            if c.isdigit() or c == "+":
                limpio += c


        if not limpio.startswith("+"):
            limpio = prefijo + limpio

        # Verificar si después del '+' todo es numérico
        if limpio.startswith("+") and limpio[1:].isdigit():
            validos.append(limpio)
        else:
            invalidos.append(numero)

    return {
        "válidos": validos,
        "inválidos": invalidos
    }


resultado = normalizar_telefonos(["95815325", "+519515482", "abz", "Fiorella"], pais_defecto="PE")
print(resultado)
