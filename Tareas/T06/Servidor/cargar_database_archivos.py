import os.path
import pickle


def cargar_database_archivos():
    if not os.path.isfile("database/database_archivos.txt"):
        with open("database/database_archivos.txt", "wb") as new:
            pickle.dump({}, new)
        return {}

    with open("database/database_archivos.txt", "rb") as database_file:
        data_dict = pickle.load(database_file)
        return data_dict
