import os.path
import json


def cargar_database_amistades():
    if not os.path.isfile("database/database_amistades.txt"):
        with open("database/database_amistades.txt", "w") as new:
            json.dump({}, new)
        return {}

    with open("database/database_amistades.txt", "r") as database_file:
        data_dict = json.load(database_file)
        return data_dict
