__author__ = 'ivania'

import json
from collections import defaultdict
start_hour = '23:30'


def read_tweet(tweet, words_frequency, players_frequency, players_names):
    # Implementar
    # Buscar palabras frecuentes
    # Revisar si las palabras corresponden a un jugador
    return words_frequency, players_frequency


def read_tweets_window(start, end, registers, players_names):
    # Implementar
    # Revisar las palabras para cada tweet si está en la ventana de tiempo
    words_frequency = {}
    players_frequency = {}
    # Filtrar palabras infrecuentes

    return words_frequency, players_frequency


def is_in_time_window(hour, start, end):
    # Implementar
    return True


def transform_event_time(minute):
    hour_s, min_s = start_hour.split(':')
    min_s = int(min_s)
    hour_s = int(hour_s)
    if min_s + minute > 59:
        if hour_s + (min_s + minute) / 60 > 23:
            hour_s = int((min_s + minute) / 60 - 1)
        min_s = (min_s + minute) % 60
    else:
        min_s += minute

    return hour_s, min_s


def frequent_words(tweets, events, players_words):
    event_statistics = {}

    for event in events:
        words_frequency = {}
        event.replace('.', '')
        event.replace(',', '')
        event.replace('¿', '')
        event.replace('?', '')
        event.replace('!', '')
        event.replace('¡', '')

        palabras_evento = event.split(' ')
        for palabra in palabras_evento:
            if len(palabra) > 4:
                if not palabra in words_frequency:
                    words_frequency.update({palabra: 1})
                else:
                    freq = words_frequency[palabra] + 1
                    words_frequency.update({palabra: freq})

        minute = events[event]

        with open('Evento{}.txt'.format(minute), 'w+') as file_words:
            for word, frequency in words_frequency.items():
                file_words.write('{}\t{}\n'.format(frequency, word))

    return event_statistics


def load_names_players(players):
    players_names = {}
    for player in players:
        nombre = player['Nombre']
        apodos = player['Apodos']
        twitter = player['Twitter']
        lista_names = [nombre, twitter] + apodos
        players_names.update({nombre:lista_names})
    return players_names

if __name__ == "__main__":

    fileplayers = open('players.json')
    players = json.load(fileplayers)
    players_words = load_names_players(players)

    tweets = {}
    tweetsfile = open('tweets.csv')

    events = {}
    eventsfile = open('events.csv')
    lineas_eventos = eventsfile.readlines()
    for evento in lineas_eventos:
        minuto = int(evento.split(',')[0])
        detalle = evento.split(',')[1]
        events.update({minuto:detalle})

    tweetsfile = open('tweets.csv', "r", encoding='ascii', errors='ignore')
    lineas = tweetsfile.readlines()
    lineas2 = []
    for linea in lineas:
        if linea != '\n':
            lineas2.append(linea[:-1])
    lineas_juntas = "".join(lineas2)
    print(lineas_juntas)
    tweets = {}
    n_brackets = 0
    for c in lineas_juntas:
        if c == '"':
            n_brackets += 1
            if n_brackets == 1:
                usuario = ""
                actual = 'usuario'
                continue
            elif n_brackets == 3:
                tiempo = ""
                actual = 'tiempo'
                continue
            elif n_brackets == 5:
                texto = ""
                actual = 'texto'
                continue
            if n_brackets == 6:
                tweets.update({tiempo[:-2]:texto})
                n_brackets = 0
        if actual == 'usuario':
            usuario += c
        if actual == 'tiempo':
            tiempo += c
        if actual == 'texto':
            texto += c

    events_statistics = frequent_words(tweets, events, players_words)
