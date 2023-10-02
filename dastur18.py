# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:03:02 2023

@author: shoki
"""
def t_ism(ism,familya):
    """To'liq ism qaytaruvchi funksiya"""
    t=f"{ism} {familya}"
    return t
talaba=t_ism("olim","hakimov")
print(talaba)



def toliq_ism(ism,familya,otasining_ismi=''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        t_ism=f"{ism} {familya} {otasining_ismi}"
    else:
        t_ism=f"{ism} {familya}"
    return t_ism.title()
talaba1=toliq_ism('jamshidbek','shokirov','azamat o\'g\'li')
talaba2=toliq_ism('oybek', 'eshonqulov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya,modeli,yili,rangi,narxi=None):
    """Bu funksiya avtomobillar haqida malumot chiqaradi"""
    avto={'kompaniya':kompaniya,
          'model':modeli,
          'yil':yili,
          'rang':rangi,
          'narx':narxi}
    return avto
avto1=avto_info('BMW','M5',2024,'qora')
avto2=avto_info('GM','Cobalt',2021,'oq',15000)
avtos=[avto1,avto2]
for a in avtos:
    if a['narx']:
        narx=a['narx']
    else:
        narx='Nomalum'
    print(f"{a['rang'].title()} {a['model']}. Narxi: {narx} ")


def oraliq(min,max,qadam=1):
    """list(range()) funksiyalar birlashmasi"""
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
print(oraliq(3,9,2))
    


def avto_info(kompaniya,modeli,yili,rangi,narxi=None):
    """Bu funksiya avtomobillar haqida malumot chiqaradi"""
    avto={'kompaniya':kompaniya,
          'model':modeli,
          'yil':yili,
          'rang':rangi,
          'narx':narxi}
    return avto
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting: ")
    kompaniya=input("Kompaniya nomi: ")
    modeli=input("Avtomobil modeli: ")
    yili=int(input("Yili: "))
    rangi=input("Rangi: ")
    avtolar.append(avto_info(kompaniya, modeli, yili, rangi))
    javob=input("Yana mashina qo'shamizmi?(ha\yoq) ")
    if javob=='yoq':
        break
    
print("Sizda bor mashinalar ro'yxati:\n")
print(avtolar)


        
#######   AMALIYOT  >>>>>>>>>>>>>

def talaba(ism, familya,t_yil,t_joy,telfon=None):
    t={"ismi":ism,
       "familyasi":familya,
       "tug'ilgan yili":t_yil,
       "tug'ilgan joyi":t_joy,
       "yoshi":2023-t_yil,
       "tel raqami":telfon
       }
    
    return t
talabalar=[]
while True:
    print("quyidagi malumotlarni kiriting: ")
    ism=input("Ism: ")
    familya=input("Familya: ")
    t_yil=int(input("Tug'ilgan yil: "))
    t_joy=input("Manzili: ")
    telfon=input("telefon raqami: ")
    javob=input("Yana ma'lumot kiritasizmi(ha\yoq): ")
    talabalar.append(talaba(ism, familya, t_yil, t_joy,telfon))
    if javob=='yoq':
        break
print(talabalar)


def katta(a,a1,a2):
    m=max(a,a1,a2)
    print(m)
    return m
katta(1,2,3)



PI=3.1428
def aylana(radius):
     r={
        "radiusi":radius,
        "diametri":radius*2,
        "uzunligi":2*PI*radius,
        "yuzasi":PI*(radius**2)
        }
     #print(aylana(radius))
     return r
radius=int(input("r="))

print(aylana(radius))



           
def t_sonlar(m,l):
    tub_sonlar=[]
    for n in  range(m,l+1):
        tub=True
        if n<=1:
            tub=False
        elif n==2:
            tub=True
                
        else:
            for j in range(2,n):
                if n%j==0:
                    tub=False
                            
        if tub:
            tub_sonlar.append(n)
    print(tub_sonlar)
    return tub_sonlar

m=int(input("1-sonni kiriting m="))
l=int(input("Oxirgi sonni kiriting l="))
t_sonlar(m, l)


def fibona(n):
    a=[]
    a.append(a1)
    a.append(a2)
    for i in range(n-2):
        b=a[i]+a[i+1]
        a.append(b)
    print(a)
    return a
n=int(input("n="))
#i=0

a1=int(input("Massivning 1-elementini kiriting: "))
a2=int(input("Massivning 2-elementini kiriting: "))

fibona(n)




                    





















