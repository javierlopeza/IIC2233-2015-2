data = {"javier":["jaja", 'jojo', "kaka"],
     "marlo": ["lala", "mumo", "perro"]}

import json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('data.txt', 'r') as outfile:
    a = json.load(outfile)

print(type(a))