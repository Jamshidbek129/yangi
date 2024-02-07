# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:58:53 2024

@author: shoki
"""
import datetime as dt
hozir=dt.datetime.now()
print(hozir)

print(hozir.date())

print(hozir.time())

print(hozir.hour)

print(hozir.minute)

print(hozir.second)

# print(hozir.date)

bugun=dt.date.today()
print(f"\n{bugun}")

ertaga=dt.date(2024,1 ,23)

print(ertaga)


vaqtHozir=dt.datetime.now().time()
print(f"Hozirgi vaqt:{vaqtHozir}")
vaqtKeyin=dt.time(0,30,5)
print(f"Men kiritgan vaqt:{vaqtKeyin}")

print(f"Kunlar farqi: {(ertaga-bugun).days} ")

fevral1=dt.datetime(2024,2,1,0,0,0)
farq=fevral1-hozir
print(farq.seconds)
print(farq.days)
soat=farq.seconds//3600
minut=farq.seconds//60-soat*60
secund=farq.seconds-minut*60-soat*3600

print(f"1-fevralgacha {farq.days} kun {soat} soat {minut} minut va {secund} secund bor")


import math 
PI=math.pi
print(PI)
E=math.e
print(E)
print(math.sin(PI/2))
print(math.cos(PI))
print(math.tan(math.pi/2))
print(math.degrees(PI))
print(math.radians(90))

###  LOGARIFMIK FUNKSIYALAR  >>>
## NATURAL LOGORIFM log(x)
print(math.log(E**4))
  ## ASOSLI LOGARIFM  >>> 
print(math.log2(8))
 

###   YAXLITLASH  >>>
a=4.8
# Yuqoriga yaxlitlash
print(math.ceil(a))
# Pastga yaxlitlash
print(math.floor(a))
# Yaxlitlash
print(round(a))

import json
import pprint
filename="bemor.json"
with open(filename) as file:
    x=json.load(file)
#a=json.dumps(x, indent=4)
print(x,"\n")

pprint.pprint(x)


print("\n\n\n")



import re
from uzwords import words
word1="темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3),"\n")

Royxat=[]
andoza2="^а.......к$"
for i in words:
    if re.match(andoza2,i):
        Royxat.append(i)
        
print(Royxat)


####  AMALIYOT  >>>>
Ramazon=dt.date(2024,3,11)
Qurbon_Hayiti=dt.date(2024,6,17)
now=dt.datetime.now()
print(f"Ramazonga {(Ramazon-now.date()).days} kun qoldi!")
print(f"Qurbon hayitiga {(Qurbon_Hayiti-now.date()).days} kun qoldi!")

tugilgan_kun=dt.date(2004,9,18)
print(f"{(now.date()-tugilgan_kun).days} ")
