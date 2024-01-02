# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:11:52 2023

@author: shoki
"""

import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,1))


daraja=lambda x,y:x**y
print(daraja(int(input("x=")),int(input("y="))))


def daraja2(n):
    return lambda x1: x1**n
kvadrat=daraja2(2)
kub=daraja2(3)
a=int(input("Son kiriting:"))
print(f"{a} ning kvadrati {kvadrat(a)} ga teng\n"
      f"{a} ning kubi {kub(a)} ga teng")



from math import sqrt
sonlar=list(range(1,5,3))
ildizlar=list(map(sqrt,sonlar))



sonlar=list(range(11))
def kvadrat(x):
    return x**2
print(list(map(kvadrat,sonlar)))

# lambda orqali ishlanishi
kvadrat2=list(map(lambda x:x**2,sonlar))
print(kvadrat2)



a=[1,2,3]
b=[4,5,6]
a_plus_b=list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

## SAMPLE HAMDA FILTERNI ISHLASHI
import random as ran
sonlar1=ran.sample(range (100), 10)
print(sonlar1)
def juft(x):
    return x%2==0
juft_sonlar=list(filter(juft,sonlar1))
print(juft_sonlar)
    

juft_sonlar1=list(filter(lambda x1:x1%2==0,sonlar1))
print("lambda",juft_sonlar1)

    
mevalar=['olma','olcha','nok','o\'rik','anor']
mevalar_o=list(filter(lambda meva:meva.startswith("o"),mevalar))
print(mevalar_o)


mevalar2=list(filter(lambda meva:len(meva)>=4,mevalar))
print(mevalar2)

mevalar3=list(filter(lambda meva:meva.startswith("a") and meva.endswith("r"),mevalar))
print(mevalar3)








































