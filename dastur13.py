# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:17:55 2023

@author: shoki
"""

talaba={
        'ism':'jamshidbek',
        'yosh':19,
        "kurs":2,
        "fakultet":"dasturiy injenering"
        }
print(talaba['yosh'])
print(talaba.items(),"\n")
son=0
for kalit, qiymat in talaba.items():
    print(f"Kalit: {kalit}")
    print(f"qiymat: {qiymat}\n") 
    son=son+1
print(son,"\n")
telefonlar={
    "Jamshid":"VIVO",
    "Farhod":"Redmi",
    "Jony":"Iphone"
    }
for k,q in telefonlar.items():
    print(f"{k} {q} telefonini ishlatadi.\n")
mahsulotlar={
    "olma":10000,
    "olcha":12000,
    "behi":15000,
    }
print(mahsulotlar.keys())
print("Do'kondagi mahsulotlar:")
for a in mahsulotlar.keys():
    print(a.title())
bozorlik=["anor","olma","behi"]
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
for a in bozorlik:
    if a not in mahsulotlar:
        print(f"Iltimos, do'koningizga {a} ham olib keling.\n")
for b in sorted(mahsulotlar):
    print(b.title())
print("\n")
print(telefonlar,"\n")
print(telefonlar.values(),"\n")
print("Foydalanuvchilar quyidagi telfonlardam foydalanadilar:\n")
for tel in telefonlar.values():
    print(tel)
    # SET metodining ishlashi
print("\n")
telefonlar={
    "Jamshid":"VIVO",
    "Farhod":"Redmi",
    "Jony":"Iphone",
    "G'ofurjon":"VIVO",
    "Hakim":"Redmi"
    }
for tel in set(telefonlar.values()):
    print(tel)
#### set malumot turi hamdir


toys={"ayiqcha","kuchukcha","mushukcha","ayiqcha"}
print(type(toys))
print(toys)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        