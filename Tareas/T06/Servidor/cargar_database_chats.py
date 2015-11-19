import os.path
import json


def cargar_database_chats():
    if not os.path.isfile("database/database_chats.txt"):
        with open("database/database_chats.txt", "w") as new:
            json.dump({}, new)
        return {}

    with open("database/database_chats.txt", "r") as database_file:
        data_dict = json.load(database_file)
        return data_dict
