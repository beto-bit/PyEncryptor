from main.funcs import modifier as mod
from main.funcs import readwrite as rw


def ascii_eq(string):
    """
    Esta función convierte una cadena de texto en su equivalente de ASCII.
    Luego suma cada uno de sus valores para arrojar un resultado.
    """
    res = 0

    for char in string:
        res += ord(char)

    return res



def encriptar(name_doc, new_name, pssw):
    """
    Tiene como entrada el nombre del archivo a "encriptar" y el nuevo
    nombre que tendrá el documento resultante. Básicamente hace el trabajo
    de encriptación.
    """
    string_list = rw.lines_generator(name_doc) # Archivo a lista
    string_list.reverse() # Ordenar al revés

    pssw = ascii_eq(str(pssw)) % 1024# Contraseña (str) a ASCII (int)

    ascii_list = mod.char_to_ascii(string_list, pssw) # Convertir a ASCII

    final_name = new_name[0: -4] + "_encriptado.txt"  # Nombre final

    rw.lines_writer(final_name, ascii_list)


def desencriptar(name_doc, new_name, pssw):
    """
    Tiene como entrada el nombre del archivo a "desencriptar" y el nuevo
    nombre que tendrá el documento resultanto. Básicamente desencripta.
    Además obtiene como entrada una contraseña (str)
    """
    str_list = rw.lines_generator(name_doc) # Archivo a lista
    str_list.reverse() # Vuelta
    
    pssw = ascii_eq(str(pssw)) % 1024# Contraseña (str) a ASCII (int)

    x = mod.ascii_to_char(str_list, pssw) # A char
    y = mod.char_to_str(x) # A str

    final_name = new_name[0: -4] + "_desencriptado.txt" # Nombre final

    rw.lines_writer(final_name, y)





