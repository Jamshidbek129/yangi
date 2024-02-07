# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:01:28 2024

@author: shoki
"""

import json
m=5
m_json=json.dumps(m)

m2=json.loads(m_json)

x=True
x_json=json.dumps(x)
print(x,x_json)


x2=json.loads(x_json)
print(x2)

sonlar1=(1,2,3,4)
print("1-",sonlar1, type(sonlar1))

sonlar2=[5,6,7,8]
print("2-",sonlar2,type(sonlar2))

sonlar1_json=json.dumps(sonlar1)
print("1-",sonlar1_json,type(sonlar1_json))
sonlar2_json=json.dumps(sonlar2)
print("2-",sonlar2_json,type(sonlar2_json))

sonlar1_1=json.loads(sonlar1_json)
print("1-",sonlar1_1,type(sonlar1_1))
sonlar2_2=json.loads(sonlar2_json)
print("2-",sonlar2_2,type(sonlar2_2))

bemor={"ism":"Azamat",
       "familya":"Quryozov",
       "dori":[{"nomi":"parasetamol", "miqdori":"0.5 ml"},
               {"nomi":"trimol"     , "miqdori":"1 ml"}],
       "farzandlar":("Jamshidbek","Sevinch","Sevila"),
       "Allergiya": None}

# b=json.dumps(bemor)
# print(b)
b=json.dumps(bemor,indent=4)
print(b)

with open("bemor.json","w") as file:
    json.dump(bemor,file)

with open('bemor.json') as f:
    b=json.load(f)

print(type(b))
print(b) 
