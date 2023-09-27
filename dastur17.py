# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:04:39 2023

@author: shoki
"""

def salom_ber(ism):
    """Salom beruvchi dastur"""
    print(f"Assalomu aleykum, {ism.title()}!")
salom_ber(input("Ismingiz: "))



##########    AMALIYOT   >>>>>>>>>>>>>>>>>>

def yosh_aniqla(ism,t_yil):
    """Bu dastur kiritilgan insonning yoshini qaytaradi"""
    print(f"{ism.title()} 2023-yilda {2023-t_yil} yoshda bo'lgan")
while True: 
    yosh_aniqla(input("Ism: "),int(input("Tug'ilgan yilni kiriting: ")))
    a=input("Dastur yana ishlasinmi?(ha\yoq) ")
    if a!='ha':
        break
a=True
def kvadrat_kub(son):
    """Bu funksiya foydalanuvchi kiritgan sonni kvadrati va kubini chiqaradi"""
    print(f"{son} ning kvadrati {son**2} ga teng\n"
f"{son} ning kubi {son**3} ga teng")
while a:
    kvadrat_kub(int(input("Son kiriting: ")))
    b=input("Dastur yana ishlasinmi?(ha\yoq) ")
    if b!='ha':
        a=False



def juft_toq(son):
    """Bu funksiya son juft yoki toq ekanligini ko'rsatadi"""
    if son%2==0:
        print("Bu son juft")
    else:
        print("Bu son toq")
while True:
    juft_toq(int(input("Son kiriting: ")))
    a=input("Yana son kiritasizmi?(ha\yoq) ")
    if a!='ha':
        break
    
    
def max_min(a,b):
    """Bu funksiya 2 sondan kattasini topadi"""
    if a>b:
        print(a)
    elif a==b:
        print("Bu sonlar teng")
    else:
        print(b)
while True:
    max_min(int(input("1-sonni kiriting: ")),int(input("2-sonni kiriting: ")))
    i=input("Yana son kiritasizmi?(ha\yoq) ")
    if i!='ha':
        break
    
    
def daraja(x,y):
    """Bu funksiya darajani aniqlaydi"""
    print(f"{x} ning {y}-darajasi {x**y}ga teng")
while True:
    daraja(int(input("Son kiriting: ")),int(input('Daraja kiriting: ')))
    a=input("Dastur yana ishlasinmi?(ha\yoq): ")
    if a!='ha':
        break
    
    
    
def daraja(x,y=2):
    """Bu funksiya darajani aniqlaydi"""
    print(f"{x} ning {y}-darajasi {x**y}ga teng")
while True:
    daraja(int(input("Son kiriting: ")))
    a=input("Dastur yana ishlasinmi?(ha\yoq): ")
    if a!='ha':
        break



def bolinish(son):
    """Bu funksiya kiritilgan son (2,10) oraliqda qaysi
        sonlarga bo'linishini ko'rsatadi"""

    for i in range(2,11):
        if son%i==0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi")
        
bolinish(int(input("Son kiriting: ")))


















