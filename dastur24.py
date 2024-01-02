# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:54:21 2023

@author: shoki
"""
from uzwords import words
import random as ran
def sozlar():
    l=[]
    j1=0
    x=ran.choice(words)
    while '-' in x or ' ' in x:
        x=ran.choice(words)
    print(x)
    y=len(x)
    print(f"Men {y} xonali so'z o'yladim.Topa olasizmi?")
    for i in range(y):
        l.append('_')
        print('_',end=' ')
    r1=''
    while True:
        r=''
        
        j=0
        if '_' in l:
            a1=input("\nHarf kiriting(kril alifbosi bilan): ")
            j1+=1
            if a1 in r1:
                print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            else:
                for i in x:
                    if a1==i:
                        l[j]=a1
                        j+=1
                        print("Bu harf men o'ylagan so'zda mavjud")
                        for i in l:
                            r=r+i+' '
                        print(r)
                        
                    
                    else:
                        j+=1
                
                r1+=a1
                print(f"Shu vaqtgacha kiritgan harflaringiz: {r1}")
        else: 
            break
    print(f"Tabriklayman! men o'ylagan so'z {x} edi.Siz buni {j1} urinishda topdingiz")
sozlar()

































































