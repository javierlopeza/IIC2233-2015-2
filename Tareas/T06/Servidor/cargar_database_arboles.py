import os.path
import pickle


def cargar_database_arboles():
    if not os.path.isfile("database/database_arboles.txt"):
        with open("database/database_arboles.txt", "wb") as new:
            pickle.dump({}, new)
        return {}

    with open("database/database_arboles.txt", "rb") as database_file:
        data_dict = pickle.load(database_file)
        return data_dict