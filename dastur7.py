# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 23:50:58 2023

@author: shoki
"""
#cars=['jentra','nexia','cobalt','tracker']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars))  #sorted listga tegmasdan uni tartiblaydi
#print(cars)
#print(sorted(cars,reverse=True))
#sonlar=[234,45.7,-98,0,3]
#print(sorted(sonlar))
#print(sonlar)
#sonlar.reverse()
#print(sonlar)
#print(len(cars))
#numbers=list(range(0,10))
#print("Numbers",numbers)
#juft_sonlar=list(range(0,21,2))
#print(juft_sonlar)
#maximal=max(juft_sonlar)
#print(maximal)
#minimal=min(juft_sonlar)
#jami=sum(juft_sonlar)
#print(minimal,"\n",jami)
#print(cars[0:3])
#print(cars[:4])
#print(cars[2:])
#my_cars=cars
#my_cars.remove('jentra')
#my_cars.remove("tracker")
#print(my_cars)
#TUPLE yani o'zgarmas ro'yxat
#oila=("Azamat","Gulshan",'Sevinch','Sevila')
#print(oila)
#oila.insert(2,"Jamshid")
#print(type(oila))
#oila=list(oila)
#print(type(oila))
#oila.insert(2,"Jamshid")
#print(oila)
#oila=tuple(oila)
#print(type(oila))
#print(oila)





davlatlar=["O'zbekiston","Qozog'iston",'Qirg\'iziston','Tojikiston','Avg\'oniston']
print(davlatlar)
a=len(davlatlar)
print(a)
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print("Reverse metodi ",davlatlar)
print("Sort metodi: ")
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
print("   ")
sonlar=list(range(120,1201,2))
print(sonlar)
b=sum(sonlar)
print(b)

c=max(sonlar)
d=min(sonlar)
print(c-d)
print(len(sonlar))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[230:250])
  

taomlar=['Barak','Go\'mma','Manti',"So'msa",'Palov']
nonushta=taomlar[:]
del nonushta[:]
nonushta.append("yog'")
nonushta.append("bol")
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)



















