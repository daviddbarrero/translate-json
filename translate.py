from googletrans import Translator

import os
import json

translator = Translator()

file = 'input.json'
finaljson = {}


with open(file) as f:
    data = json.load(f)

for idx, i in enumerate(data):
    # Change output language by adding this to the next line :
    # translation = translator.translate(data[i], *LANGUAGE OF OUTPUT*  )
    translation = translator.translate(data[i])
    print(translation.text)
    data[i] = translation.text


with open('translation.json','w') as f:
    json.dump(data, f, indent=4)



