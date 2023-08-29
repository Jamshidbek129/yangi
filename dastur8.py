# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:35:28 2023

@author: shoki
"""

#mehmonlar=['Ali','Vali','Jamshid','Ruxsora']
#mehmonlar.sort()
#for mehmon in mehmonlar:
#    print("Salom",mehmon)
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon} sizni 18-sentabr kuni Saltanat restoraniga taklif qilamiz")
#    print("Hurmat bilan Jamshidbek!!!\n")
#s=list(range(1,101))
#for i in s:
 #  print(f"{i}ning kvadrati {i**2}ga teng")
#sonlar=list(range(11))
#sonlar_kubi=[]
#for son in sonlar:
 #   sonlar_kubi.append(son**3)
#print(sonlar)
#print(sonlar_kubi)
#dostlar=[]
#print("5 ta do'stingizni kiriting\n")
#for i in range(5):
#    dostlar.append(input(f"{i+1}-do'stingizni kiriting>>>"))
#dostlar.sort()
#print(dostlar)


##### AMALIYOT>>>>>>
ismlar=['Jamshid','Ruxsora','Farhod','Mohinur','Jahongir']
ismlar.sort()
print(ismlar)
n=0
for a in ismlar:
    print(f"Salom {a}.Menga nomeringni ayt.")
    n=n+1
print(f"Kod {len(ismlar)} marta takrorlandi")
print("kod",n,"marta takrorlandi")
sonlar=list(range(11,100,2))
for i in sonlar:
    print(f"{i}ning kubi {i**3}ga teng\n")
kinolar=[]
print("5 ta filmnomini kiriting:")
for n in range(5):
    kinolar.append(input(f"{n+1}-kino nomi:"))
kinolar.sort()
print(kinolar)
odamlar=[]
j=int(input("bugun nechta odam bilan suhbatlashdingiz?>>>"))
for l in range(j):
    odamlar.append(input(f"{l+1}-suhbatlashgan odamingiz kim edi?>>>"))
print(sorted(odamlar))







