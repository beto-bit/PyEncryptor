def lines_generator(name_doc):
    """
    Esta función crea una lista con las líneas del documento.
    """
    with open(name_doc, 'r', encoding="utf-8") as f:
        # Generar lista
        lista = []

        for linea in f:
            lista.append(linea)

        return lista


def lines_writer(name_doc, lista):
    """
    Esta función escribe en un documento tomando como argumento el nombre
    del documento y la lista que contiene las diversas líneas del mismo.
    Se encarga de que se inserten en líneas nuevas siempre (que sea necesario).
    
    En caso de que se genere un error debido a la introudcción de caracteres
    incompatibles (y por ende un error en la contraseña) escribe los caracteres
    usando bits y en 'utf-8'.
    """
    try:
        with open(name_doc, 'w') as f:
            for linea in lista:
                if linea[-1] == "$":
                    f.write(linea + "\n")
                else:
                    f.write(linea)
    except:
        with open(name_doc, 'wb') as f:
            for linea in lista:
                f.write(linea.encode('utf-8'))

