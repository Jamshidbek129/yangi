# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:23:13 2023

@author: shoki
"""
import json
x=10
x_j=json.dumps(x)
print(type(x_j))

m=True
m_J=json.dumps(m)
print(type(m))
print(m_J)
print(json.loads(m_J))

sonlar=(1,2,3,4)
sonlar_json=json.dumps(sonlar)
print(type(sonlar))
print(sonlar)
print(sonlar_json)
print(type(sonlar_json))

print(type(json.loads(sonlar_json)))


bemor={"ism":"Azamat",
       "familya":"Quryozov",
       "dori":[{"nomi":"parasetamol", "miqdori":"0.5 ml"},
               {"nomi":"trimol"     , "miqdori":"1 ml"}],
       "farzandlar":("Jamshidbek","Sevinch","Sevila"),
       "Allergiya": None}
b=json.dumps(bemor)
print(b)

b=json.dumps(bemor, indent=4)
print(b)
