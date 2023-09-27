# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:51:16 2023

@author: shoki
"""

ismlar=[]
n=1
while True:
    ism=input(f"{n}-do'stingizni ismini kiriting: ")
    ismlar.append(ism)
    n+=1
    l=input("Yana ism kiritasizmi?(ha\yo'q): ")
    if l=='yo\'q':
        break
print("Do'slaringiz ro'yhati:")   
for i in ismlar:
    print(i.title())
    
    

dostlar={}
n=1
while True:
    ism=input(f"{n}-do'stingizni ismini kiriting: ")
    yosh=int(input(f"{ism.title()}ning yoshini kiriting: "))
    dostlar[ism]=yosh
    l=input("Yana ism kiritasizmi?(ha\yo'q): ")
    n+=1
    if l=='yo\'q':
        break
for i,j in dostlar.items():
    print(f"{i.title()}ning yoshi {j}")    
    
    

cars=['malibu','cobalt','jentra','BMW','matiz','nexia','matiz']
car='matiz'
while car in cars:
    cars.remove(car)
print(cars)
    

talabalar=['jamshidbek','oybek','asror','rustam','raxim']
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=int(input(f"{talaba.title()}ning bahosini kiriting: "))
    print(f"{talaba.title()} baholandi!")
    baholangan_talabalar[talaba]=baho
for i,j in baholangan_talabalar.items():
    print(f"{i.title()}ning bahosi {j}")
    

############    AMALIYOT   >>>>>>>>>


mahsulotlar=[]
a=True
n=1
while a:
    b=input(f"{n}-mahsulot nomini kiriting: ")
    mahsulotlar.append(b)
    c=input("Yana mahsulot kiritasizmi?(ha\yo'q): ")
    n+=1
    if c!='ha':
        a=False
print(mahsulotlar)


n1=1
a1={}
while True:
    b1=input(f"{n1}-mahsulot nomini kiriting: ")
    narx=int(input(f"{b1}ning narxini kiriting: "))
    a1[b1]=narx
    c1=input("Yana mahsulot kiritasizmi?(ha\yo'q):  ")
    n1+=1
    if c1!='ha':
        break
print(a1)
    
for a2,i2 in a1.items():
    if a2 in mahsulotlar:
        print(f"{a2}ning narxi {i2}")
    else:
        print(f"Bizda {a2} nomli mahsulot yo'q")























