import os.path


def cargar_database_usuarios():
    if not os.path.isfile("database/database_usuarios.txt"):
        open("database/database_usuarios.txt", "w")
        return {}

    with open("database/database_usuarios.txt", "r") as database_file:
        data_dict = {}

        for linea in database_file.readlines():
            usuario = linea.split("\t")[0]
            salt = linea.split("\t")[1]
            clave_salt_hash = linea.split("\t")[2][:-1]

            data_dict.update({usuario: (salt, clave_salt_hash)})

        return data_dict
