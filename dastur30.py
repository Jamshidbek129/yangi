# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:25:03 2023

@author: shoki
"""
from Classlar import dost, Shaxs
Hakim=dost("Hakim", 2001, "Xiva",22)
Abbos=dost("Abbos",2004,"Yangiariq",19)
Sanjar=dost("Sanjar",2004,"Yangiariq",19)

print(Hakim)
print(Hakim<=Abbos)
print(Hakim>Abbos)
print(Sanjar==Abbos)


from Classlar import Avto,Avtosalon
avto1=Avto("Gm","Cobalt","oq",2021,15000,10000)
avto2=Avto("Gm","Malibu","qora",2023,45000)
avto3=Avto("BMW","M5","qora",2024,150000)
avto4=Avto("BMW","X7","Oq",2024,180000)
avto5=Avto("Bugatti","Chiron","qora",2030,100000)
salon1=Avtosalon("AzamatAvto")
salon2=Avtosalon("GulshanAvto")
salon1.add_avto(avto1,avto2,avto3)
print(salon1)
print(salon1[:])
salon1[0]=Avto("BMW","M3","qora",2024,130000)
print(salon1[0])
salon2(avto1,avto4)
print(salon1())
salon3=salon1+salon2
print(salon3)
print(salon3[:])
    
salon1+avto5
print(salon1[:],"\n\n")






####   AMALIYOT  >>>>>>>>
A1=Shaxs("Jamshidbek","Shokirov",2004,"AD0417816")
A2=Shaxs("Abdulaziz","Berdiqulov",2005,"AD0417817")
print(A1)
print(A2<=A1)
print(A2>A1)
print(A1.get_age(2023),"\n")


from Classlar import Fan
S1="Jamshidbek"
S2="Oybek"
matem=Fan("Matematika")
fizika=Fan("Fizika")
fizika+S1



matem.add_student(S1,S2)
print(matem)

print(matem[:])
matem[1]="Abdulaziz"
print(matem[:])
print(len(matem))

S3="Rustam"
matem+S3
print(matem[:])

matem-S1
print(matem[:],"\n")

print(matem(),"\n")

print(matem("Abdulaziz",'Rustam'))