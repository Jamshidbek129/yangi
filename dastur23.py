# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:45:18 2023

@author: shoki
"""
import random as ran
k=True
print("Keling son topish o'yinini o'ynaymiz!")
o=int(input("Nechigacha bo'lgan sonlar orasida o'ynaymi? "))
while k:
    i=1
    a=ran.randint(1,o)
    print(f"1 dan {o} gacha son o'yladim topa olasizmi?")
    while True:
    
    
        x=int(input(">>>"))
        if a>x:
            print("Xato! Men o'ylagan son bundan kattaroq, yana urinib ko'ring:")
            i+=1
        elif a<x:
            print("Xato! Men o'ylagan son bundan kichikroq, yana urinib ko'ring:")
            i+=1
        else:
            print(f"To'g'ri! Men {x} ni o'ylagan edim! Siz buni {i} urinishda topdingiz. TABRIKLAYMAN!")
            break
    j=1
    print(f"1 dan {o} gacha son o'ylang va men topishga harakat qilaman")
    b=input("O'ylagan bo'lsangiz istalgan harfni bosing: ") 
    past=1
    tepa=o
    while True:
        a1=ran.randint(past, tepa)
        a2=input(f"Siz {a1} ni o'yladingiz: to'g'ri(t), kattaroq(+),kichikroq bo'lsa(-)")
        if a2=="+":
            past=a1+1
            j+=1
        elif a2=='-':
            tepa=a1-1
            j+=1
        else:
            print(f"Men siz o'ylagan sonni {j} urinishda topdim!")
            break
    if i==j:
        print("Durrang")
    elif i<j:
        print(f"Siz {j} u {i} hisobida yutdingiz")
    else:
        print(f"Siz {i} u {j} hisobida yutqazdingiz")
    javob=input("Yana o'ynaymizmi?(ha\yoq)")
    if javob=="yoq":
        k=False            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
