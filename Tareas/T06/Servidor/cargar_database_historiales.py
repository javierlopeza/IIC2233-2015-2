import os.path
import json


def cargar_database_historiales():
    if not os.path.isfile("database/database_historiales.txt"):
        with open("database/database_historiales.txt", "w") as new:
            json.dump({}, new)
        return {}

    with open("database/database_historiales.txt", "r") as database_file:
        data_dict = json.load(database_file)
        return data_dict
