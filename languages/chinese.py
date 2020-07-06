from googletrans import Translator

import os
import json

translator = Translator()

file = '../data/en.json'
finaljson = {}


with open(file) as f:
    data = json.load(f)

for idx, i in enumerate(data):
    # Here you can change the lenguage
    translation = translator.translate(data[i] ,'ko' )
    print(translation.text)
    data[i] = translation.text


with open('chinese.json','w') as f:
    json.dump(data, f, indent=4)

