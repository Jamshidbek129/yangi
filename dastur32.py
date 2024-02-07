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

with open("bemor.json","w") as file:
    json.dump(bemor,file)

with open('bemor.json') as f:
    b=json.load(f)

print(type(b))
print(b) 


####################    AMALIYOT    >>>>>>>>>>>>>>>>>>
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json=json.dumps(data)
print(data_json)



talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
print(talaba["ism"],talaba["familiya"])

with open("data.json","w") as file:
    json.dump(data,file)
    
with open("talaba.json","w") as f:
    json.dump(talaba,f)

with open("students.json") as f:
    b=json.load(f)
    
    
for i in b["student"]:
    print(f"{i['name']} {i['lastname']} , {i['year']}-kurs , {i['faculty']} fakulteti talabasi")
    
    
    
    
with open("__pycache__/api-result.json") as file:
    x=json.load(file)
print(x["query"]["pages"]["13801"]["title"])
print(x["query"]["pages"]["13801"]["extract"])




































