from googletrans import Translator

import os
import json

translator = Translator()

# English to spanish
file = '../data/en.json'
finaljson = {}


with open(file) as f:
    data = json.load(f)

for idx, i in enumerate(data):
    # Here you can select any lenguage
    translation = translator.translate(data[i], dest='es')
    print(translation.text)
    data[i] = translation.text


with open('spanish.json','w') as f:
    json.dump(data, f, indent=4)

