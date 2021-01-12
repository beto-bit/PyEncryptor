from funcs import modifier as mf
from funcs import read_write as rw

def encrypt(name_doc, pwd):
    """
    Esta función hace todo el trabajo de encriptación.
    """
    # Abrir archivo y crear objeto
    file = rw.reader(name_doc)
    encrypt_object = mf.Crypter(file) 
    
    # Contraseña y a UNICODE
    pwd = mf.str_to_num(pwd)
    encrypt_object.to_unicode(pwd)

    # De nuevo a caracteres
    encrypt_object.to_char(0)

    # Nuevo nombre
    new_name = name_doc[0:-4] + "_encriptado.txt"

    rw.writer(new_name, encrypt_object.gen)

def dencrypt(name_doc, pwd):
    """
    Esta función hace todo el trabajo de desencriptado.
    """
    # Abrir Archivo
    file = rw.reader(name_doc)
    dencrypt_object = mf.Crypter(file)

    # Comtraseña y a UNICODE
    pwd = mf.str_to_num(pwd)
    dencrypt_object.to_unicode(-pwd)

    # De nuevo a caracteres 
    dencrypt_object.to_char(0)

    # Nuevo nombre
    new_name = name_doc[0:-4] + "_desencriptado.txt"

    rw.writer(new_name, dencrypt_object.gen)
