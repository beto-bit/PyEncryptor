"""
Este módulo se encarga de modificar los textos de diversas formas, con el
objetivo de hacer el trabajo de encriptación. 
"""

# CLASE ENCRIPTAR-DESENCRIPTAR==================================================
class Crypter():
    """
    Esta clase contiene los métodos y atributos de un objeto destinado a 
    'encriptar' estas cadenas.
    """
    def __init__(self, gen):
        self.gen = gen

    # Encriptar
    def to_unicode(self, pwd):
        """
        Básicamente se encarga de leer cada caracter y pasarlo a su equivalente 
        ASCII. Recibe como argumentos una "contraseña", el cual corresponde a un
        número.  
        """
        temp_gen = self.gen

        def new_gen():
            for char in temp_gen():
                yield abs(ord(char) + pwd)

        self.gen = new_gen

    # Desencriptar
    def to_char(self, pwd):
        temp_gen = self.gen

        def new_gen():
            for num in temp_gen():
                yield chr(abs(num - pwd) % 1114111) 
                # Pongo el número 1114111 porque según la documentación de la
                # función "chr" el número que se le introduzca debe de estar 
                # entre 0 y 0x10ffff (inclusivo).

        self.gen = new_gen
