"""
Este módulo contiene las diversas funciones que permiten la lectoescritura de
diversos documentos.
"""

def reader(name_doc):
    """
    Esta función se encarga de crear un objeto generador con todos las líneas
    del documento. Luego, retorna ese objeto.

    El propósito de crear un generador con las LINEAS y no con los CARACTERES
    es para equilibrar el número de pasos a realizar por la computadora, y 
    la memoria RAM utilizada. De forma que se busca un equilibrio sano.
    """
    # Creando el generador
    def gen():
        with open(name_doc, 'r', encoding="utf-8") as f:
            for line in f:
                yield line

    return gen
            



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

