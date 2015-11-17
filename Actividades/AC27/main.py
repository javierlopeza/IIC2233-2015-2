# coding=utf-8
import requests
import json
from requests.auth import HTTPBasicAuth
import operator


# Debe tener los atributos:
# * _id (string)
# * name (string)
# * votes (diccionario string: int)
class Table:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name
        self.votes = {}


if __name__ == '__main__':
    USERNAME = "napoleon"
    PASSWORD = "macoy123"

    listas = requests.get('http://votaciometro.cloudapp.net/api/v1/lists', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    listas = listas.json()

    listas_candidatas = {}
    for lista in listas:
        listas_candidatas.update({lista: 0})

    tables = requests.get('http://votaciometro.cloudapp.net/api/v1/tables', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    tables = tables.json()

    mesas = []

    for mesa in tables:
        i = mesa["_id"]
        n = mesa["name"]
        nueva_mesa = Table(i, n)
        mesas.append(nueva_mesa)

    for mesa in mesas:
        info_mesa = requests.get('http://votaciometro.cloudapp.net/api/v1/tables/{}'.format(mesa._id),
                                 auth=HTTPBasicAuth(USERNAME, PASSWORD))
        info_mesa = info_mesa.json()
        for lista_candidata in info_mesa["votes"].keys():
            listas_candidatas[lista_candidata] += info_mesa["votes"][lista_candidata]

    print("VOTOS POR LISTA HASTA EL MOMENTO:")
    for lista in listas_candidatas.keys():
        print("\t{0}: {1} votos".format(lista, listas_candidatas[lista]))
    ganador_ahora = max(listas_candidatas, key=listas_candidatas.get)
    print()
    print("LISTA CON MAYORIA DE VOTOS HASTA EL MOMENTO: {}".format(ganador_ahora))
