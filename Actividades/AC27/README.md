## Actividad 27

## Usage:

See all available commands and options:
```
 python main.py --help
```

Help menu:
````
usage: main.py [-h] -u USER -p PASSW obtener

Resultados Votaciones

positional arguments:
  obtener               Obtener resultados votaciones

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Username
  -p PASSW, --passw PASSW
                        Password
````

## Example:

## Using full-name flags:

```` python main.py obtener -user USER123 -passw PPP123````

## Short version:

```` python main.py obtener -u USER123 -p PPP123 ````

## Output:
````
VOTOS POR LISTA HASTA EL MOMENTO:
        Solidaridad: 2839 votos
        Crecer: 1363 votos
        1A: 1507 votos
        Nau!: 2268 votos

LISTA CON MAYORIA DE VOTOS HASTA EL MOMENTO: Solidaridad
````
