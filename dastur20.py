# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:38:28 2023

@author: shoki
"""

def summa(*a):
   """kiritilgan sonlarning yig'indisini chiqaradi"""
   yigindi=0
   for i in a:
       yigindi+=i
   return yigindi
  
print(summa(1,2,3,4,5))
    
### yoki bunday yozsa ham bo'ladi >>>
def summa(*a1):
    yigindi=sum(a1)
    return yigindi
print(summa(1,2,3,4,5,6))


### majburiy argument ham qo'shsak bo'ladi  >>>
def summa(x,y,*a2):
    yigindi=x+y+sum(a2)
    return yigindi
print(summa(1,2,3,4,5,6,7))


def avto_info(kompaniya,modeli,**yana):
    """Bu funksiya avtomobillar haqida malumot chiqaradi"""
    yana['kompaniya']=kompaniya
    yana['model']=modeli
    return yana
print(avto_info("GM","Cobalt", rang="oq",yil=2021))


#######  AMALIYOT >>>>>>>>>>>>

def kopaytma(*sonlar):
    a=1
    for i in sonlar:
        a=a*i
    return a
print(kopaytma(22,3))


def talaba(ism,familya,**malumot):
    malumot['ismi']=ism
    malumot['familyasi']=familya
    return malumot
print(talaba("Jamshidbek","Shokirov",universitet="TATU",kurs=2))











