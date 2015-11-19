import hashlib
from random import choice
import string


def hashear(clave):
    # Se crea un SALT aleatorio.
    salt = "".join([choice(string.ascii_lowercase + "0123456789") for i in range(20)])
    clave_salt = clave + salt
    clave_salt_enc = clave_salt.encode()
    clave_hash = hashlib.sha1(clave_salt_enc).hexdigest()
    # Se retorna el SALT, CLAVEHASHEADA
    return salt, clave_hash
