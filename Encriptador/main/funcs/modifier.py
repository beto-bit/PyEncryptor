"""
Este módulo contiene las funciones que se utilizan para la edición de los diversos
documentos, básicamente las funciones que hacen el trabajo de encriptación.
"""

def list_to_string(lista, separador=""):
    """
    Convierte una lista a una cadena de texto poniendo entre espacio de la lista
    el símbolo correspondiente al separador.
    """
    str1 = ""

    for elemento in lista:
        str1 += elemento + separador

    return str1


def char_to_ascii(lista, pssw):
    """
    Esta función es la que convierte cada caracter de la lista anterior en
    su código ASCII, luego, se le suma la pssw (int) que se le intrduce, 
    dejando un "$" entre cada caracter. Devuelve esa lista.
    """
    new_lista = [] # Creación de lista contenedora de salida
    i = 0 # contados

    for linea in lista:
        new_lista.append("") # Creación de nueva 
        
        for chara in linea:
            new_chara = str(ord(chara) + pssw) + "$" # Convertir a ASCII y añadir "$"
            new_lista[i] += new_chara

        i += 1

    return new_lista


def ascii_to_char(lista, pssw):
    """
    Convierte los elementos de una lista (strings) usando el siguiente criterio:
    Toma el número correspondiente, separado por un "$" y toma ese valor y le 
    resta el pssw(int) para devolver una lista con el equivalente en ASCII.

    En caso de que el valor que examina (dentro de la lista) sea mayor a 255 
    usa la división con residuo y examina ese valor.
    """
    salida = []
    new_lista = [] # lista con los valores ASCII
    listori = [] # lista temporal que sirve de puente entre listas

    # Bucle para añadir listas embedidas a new_lista
    for elemento in lista:
        lista_temp = elemento.split("$") 
        lista_temp.pop() 

        # Bucle para hacer todos los elementos anteriores en (int)
        for numero in lista_temp:
            listori.append(int(numero) - pssw)

        new_lista.append(listori)

        listori = [] # Reiniciar listori

    # Bucle para convertir cada valor ASCII a caracter
    for mini in new_lista:
        listica = [] # init lista para contenedor en new_lista
        for number in mini:
            listica.append(chr(abs(number))) # TODO si no funciona esto ponerle el %255
        
        salida.append(listica)

    return salida

def char_to_str(lista):
    """
    Esta función convierte una colección de caracteres a una cadena de texto. 
    Está especialmente diseñada para examinar los valores que están dentro de
    una lista anidada. Devuelve esa lista.
    """
    salida = []
    
    for elemento in lista:
        listori = "" # string temporal

        for char in elemento:
            listori += char
        
        salida.append(listori)

    return salida



