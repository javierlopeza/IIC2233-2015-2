import threading
from time import sleep

def imprimir():
    i = 0
    while i < 10:
        print(i + 1)
        i += 1
        sleep(1)


t1 = threading.Thread(target=imprimir)
t1.setDaemon(True)
t1.start()
t1.join()
print("y")
