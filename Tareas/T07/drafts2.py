import dropbox
import dropbox.files
import os
import threading
from time import sleep

import dropbox
TOKEN = "YcVU8NoY5R8AAAAAAAAPaBxOhsWFLGNcvr1_YE7DyI-IdL6_3it4LIBX5E6crj_y"
dbx = dropbox.Dropbox(TOKEN)
user_info = dbx.users_get_current_account()
print(type(user_info.name.display_name))
print(user_info.name.given_name)
print(user_info.name.surname)
print(user_info.name.familiar_name)

a = "Hola: "
print(a.split(": ")[1])

print(os.path.splitext("javier.pdf")[1])

TOKEN = "YcVU8NoY5R8AAAAAAAAPaBxOhsWFLGNcvr1_YE7DyI-IdL6_3it4LIBX5E6crj_y"

dbx = dropbox.Dropbox(TOKEN)

dbx.users_get_current_account()

dbx.files_move('/IFTTT/Instagram', '/IFTTT/Instagram')