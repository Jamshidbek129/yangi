# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:27:48 2023

@author: shoki
"""

def avto_info(kompaniya,modeli,yili,rangi,narxi=None):
    """Bu funksiya avtomobillar haqida malumot chiqaradi"""
    avto={'kompaniya':kompaniya,
          'model':modeli,
          'yil':yili,
          'rang':rangi,
          'narx':narxi}
    return avto


def avto_kirit():
    """foydalanuvchi avto_info funkisayi yordamida malumotlar kiritadi"""
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
    return avtolar

def info_print(avto_info):
    """Bu funksiya avto_info va avto_kiritni birlashtiradi"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya']}."
          f"Narxi: {avto_info['narx']}")
    return avto_info