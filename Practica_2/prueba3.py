
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
