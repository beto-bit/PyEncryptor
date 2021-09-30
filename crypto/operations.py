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


def basic_encryption(filepath: Path, override=False) -> bytes:
    """Encrypts a file using a generated key, writes the key in the
    same folder as the file and then returns the key"""
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
    


basic_encryption(Path('a.txt'), True)