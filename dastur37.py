# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:33:28 2024

@author: shoki
"""
from googletrans import Translator
tarjimon=Translator()
matn="Salom dunyo"
tarjima=tarjimon.translate(matn)
print(tarjima.origin)
print(tarjima.text)

tarjima_ru=tarjimon.translate(matn, dest="ru")
print(tarjima_ru.text)
matn2="The most popular movies-'Avangers' , 'Avatar'"
tarjima_uz=tarjimon.translate(matn2, dest="uz")
print(tarjima_uz.text)


import requests
from pprint import pprint
sahifa="https://python.sariq.dev/last-words/39-pip-pypi"
m=requests.get(sahifa)
pprint(m.text)
mamlakat="Makka"
from fuzzywuzzy import fuzz , process
print(fuzz.ratio("salom","salim"))

from uzwords import words
text="абдо"
sozlar=process.extract(text, words,limit=3)
soz=process.extractOne(text, words)
print(soz)