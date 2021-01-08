"""
Este módulo contiene las diversas funciones que permiten la lectoescritura de
diversos documentos.
"""

def reader(name_doc):
    """
    Esta función se encarga de crear un objeto generador con todos las líneas
    del documento. Luego, retorna ese objeto. Recibe como argumento el nombre
    del documento del cual genera el objeto generador.
    """

    # El propósito de crear un generador con las LINEAS y no con los CARACTERES
    # es para equilibrar el número de pasos a realizar por la computadora, y 
    # la memoria RAM utilizada. De forma que se busca un equilibrio sano.

    # Creando el generador
    def gen():
        with open(name_doc, 'r', encoding="utf-8") as f:
            for line in f:
                yield line

    return gen

def writer(name_doc, gen):
    """
    Esta función escribe en un documento (name_doc) las líneas que recibe de
    parte del generador que se le pasa como argumento (gen).
    """

    with open(name_doc, "w", encoding="utf-8") as f:
        for line in gen():
            f.write(line)

