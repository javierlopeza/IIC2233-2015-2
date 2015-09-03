from utils.parser import ApacheLogsParser
from functools import reduce


class BigAnalizador:
    def __init__(self, logs):
        self.logs = logs
        self.bytes = 0
        self.errores = 0
        self.exitos = 0

    def bytes_transferidos(self):
        print(reduce(self.bytes.__add__, map(self.logs, lambda x: x.size)))

    def errores_servidor(self):
        errores = (404, 500, 501)
        print(reduce(self.errores.__add__, map(self.logs, lambda x: 1 if x.status in errores else 0)))

    def solicitudes_exitosas(self):
        exitos = (200, 302, 304)
        print(reduce(self.exitos.__add__, map(self.logs, lambda x: 1 if x.status in exitos else 0)))

    def url_mas_solicitada(self):
        urls = dict()
        map(self.logs, lambda x: urls[x.request] = 1 if x.url not in urls.keys() else urls[x.url] = 9)
        pass

if __name__ == '__main__':
    parser = ApacheLogsParser("./utils/nasa_logs_week.txt")
    logs = parser.get_apache_logs()
    biganalizador = BigAnalizador(logs)

    biganalizador.bytes_transferidos()
    biganalizador.errores_servidor()
    biganalizador.solicitudes_exitosas()
    biganalizador.url_mas_solicitada()
