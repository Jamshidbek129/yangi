# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:59:51 2023

@author: shoki
"""
from Classlar import Avto

Avto1=Avto("GM","Cobalt","Oq",2021,15000,10000)
    
print(Avto.get_num_Avto())

#### AMALIYOT   >>>>>
from Classlar import Shaxs
inson1=Shaxs("Jamshidbek", "Shokirov", 2004, "AD0417816")
inson3=Shaxs("Abbos", "Bekturdiyev", 2004, "AD0417817")
inson2=Shaxs("Jahongir", "Rustamov", 2004, "AD0417818")

print(inson1.name)
print(inson1.get_ID())
print(Shaxs.odamlar_soni)
print(inson1.get_odamlar())









