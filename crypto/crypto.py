import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def encrypt_file(key: bytes, filepath: str) -> None:
    """Encrypts a file."""
    # Using the generated key
    fernet = Fernet(key)

    # Open the original file
    with open(filepath, 'rb') as file:
        original = file.read()
        file.close()

    # Encrypting
    encrypted = fernet.encrypt(original)

    # Writing the encripted file
    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        encrypted_file.close()

def decrypt_file(key: bytes, filepath: str, readonly=False) -> bytes:
    """Decrypts a file."""
    fernet = Fernet(key)

    # Open the file
    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()
        enc_file.close()

    decrypted = fernet.decrypt(encrypted)

    # Write the decripted data
    if not readonly:
        with open(filepath, 'wb') as dec_file:
            dec_file.write(decrypted)
            dec_file.close()

    return decrypted

def generate_key() -> bytes:
    """Simple encapsulator to generate key."""
    return Fernet.generate_key()

def generate_filekey(path: str) -> bytes:
    """Generates a filekey in the specified path; returns the key"""
    key = Fernet.generate_key()

    # Generate the filekey
    with open(path + 'filekey.key', 'wb') as filekey:
        filekey.write(key)
        filekey.close()

    return key

def generate_saltfile(path: str) -> bytes:
    """Generates and store salt in the salt.key file. Returns the salt."""
    salt = os.urandom(16)

    # Store the salt in the salt.key file
    with open(path + 'salt.key', 'wb') as saltfile:
        saltfile.write(salt)
        saltfile.close()

    return salt

def generate_key_from_psw(psw: bytes, salt: bytes) -> bytes:
    """It receives password and salt, and returns a cryptographic key."""
    # Generate key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=32_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(psw))

    return key
    