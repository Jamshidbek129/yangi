# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:56:28 2023

@author: shoki
"""

def baholash(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=int(input(f"Talaba {ism.title()}ning bahosi: "))
        baholar[ism]=baho
    print(baholar)   
    return baholar
ismlar=['jamshidbek','oybek','farhodjon','adham']
baholash(ismlar[:])
 
    
    
###############  AMALIYOT  >>>>>>>>>>>>>

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].capitalize()
    return matnlar
ismlar=['jamshidbek tatu','sarvar urdu']   
katta_harf(ismlar)
print(ismlar)
  
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].capitalize()
    return matnlar
ismlar=['jamshidbek tatu','sarvar urdu']   
yangi_ismlar=katta_harf(ismlar[:])
print(yangi_ismlar)
print(ismlar)  



def baholash(ismlar):
    baholar={}
    for ism in ismlar:
        
        baho=int(input(f"Talaba {ism.title()}ning bahosi: "))
        baholar[ism]=baho
    print(baholar)   
    return baholar
ismlar=['jamshidbek','oybek','farhodjon','adham']
baholash(ismlar[:])




   
    

    
    
    






