from cryptography.fernet import Fernet

def encrypt_file(key: bytes, path: str):
    """Encrypts a specified file."""
    # Using the generated key
    fernet = Fernet(key)

    # Open the original file
    with open(path, 'rb') as file:
        original = file.read()
        file.close()

    # Encrypting
    encrypted = fernet.encrypt(original)

    # Writing the encripted file
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        encrypted_file.close()


def decrypt_file():
    pass

def generate_key() -> bytes:
    """Simple encapsulator to generate key."""
    return Fernet.generate_key()

def generate_filekey(path='') -> None:
    """Generates a filekey in the specified path."""
    key = Fernet.generate_key()

    # Generate the filekey
    with open(path + 'filekey.key', 'wb') as filekey:
        filekey.write(key)
        filekey.close()
