# -*- coding: utf-8 -*-


import dropbox
import dropbox.files
import time
import threading
import os

os.makedirs("C:\\Users\\Javier\\Desktop\\Mis Descargas2")



a = "//hola"
print(a.replace('//', "/"))
TOKEN = "YcVU8NoY5R8AAAAAAAAPaBxOhsWFLGNcvr1_YE7DyI-IdL6_3it4LIBX5E6crj_y"

dbx = dropbox.Dropbox(TOKEN)

dbx.users_get_current_account()

def f(dbx):
    b = dbx.files_list_revisions('/Certificado FCE/hola1.txt', limit=99)

    for e in b.entries:
        time.sleep(1.5)
        print(e)

l = ["Certificados", "fce"]
l = l[:-1]
print(    "/".join(l) + "/" + "minombre.jpg")



a = os.path.split("/Hola")
print(a[0])
#dbx.files_download_to_file("C:\\Users\\Javier\\Desktop\\Mis Descargas\\DOWNLOADED Josefa Y Jorge.jpg", "/IFTTT/Instagram/Josefa Y Jorge.jpg", rev=None)
archivo = open("C:\\Users\\Javier\\Desktop\\Mis Descargas\\fb_vector.pdf", "rb")
dbx.files_upload(archivo, '/fb_vector.pdf')
archivo.close()