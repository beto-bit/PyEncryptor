from os import name
from crypto.crypto import encrypt_file, decrypt_file
from crypto.crypto import generate_key, generate_filekey, \
                          generate_saltfile ,generate_key_from_psw

from pathlib import Path
from shutil import copyfile


def get_path(filepath: Path) -> str:
    """Returns the path (without name) of filepath."""
    name_len = len(filepath.name)
    return str(filepath)[0: -name_len]

# Yes. This function should be in crypto.py
def read_file(filepath) -> bytes:
    """Reads a file."""
    with open(filepath, 'rb') as f:
        content = f.read()
        f.close()

    return content


# Basic encryption/decryption funcs
def basic_encryption(filepath: str, override=False) -> bytes:
    """Encrypts a file using a generated key, writes the key in the
    same folder as the file and then returns the key"""
    filepath = Path(filepath)
    path = get_path(filepath)
    key = generate_filekey(path)

    # Override options
    if override:
        encrypt_file(key, str(filepath))
    else:
        new_filepath = path + filepath.stem + '_crypted' + filepath.suffix
        copyfile(str(filepath), new_filepath)
        encrypt_file(key, new_filepath)

    return key
    
def basic_decryption(filepath: str) -> None:
    """Decrypts a file using the generated filekey."""
    filepath = Path(filepath)
    path = get_path(filepath)

    key = read_file(path + 'filekey.key')

    decrypt_file(key, str(filepath))


# Encryption/decryption with password
def encryption_with_psw(filepath: str, psw: bytes, override=False) -> None:
    """Encrypts a file using a given password, then storing the
    salt in a separate file, in order to replicate the key."""
    filepath = Path(filepath)
    path = get_path(filepath)
    
    # Generate key
    key = generate_key_from_psw(    
        psw, 
        generate_saltfile(path)
    )

    # Override Options
    if override:
        encrypt_file(key, str(filepath))
    else:
        new_filepath = path + filepath.stem + '_crypted' + filepath.suffix
        copyfile(str(filepath), new_filepath)
        encrypt_file(key, new_filepath)

def decryption_with_psw(filepath: str, psw: bytes) -> None:
    """Decrypts a file using a given password."""
    path = get_path(Path(filepath))

    # Generate again the key
    key = generate_key_from_psw(
        psw,
        read_file(path + 'salt.key')
    )

    # Decrypt
    decrypt_file(key, filepath)
    