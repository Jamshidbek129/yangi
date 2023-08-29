# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:26:32 2023

@author: shoki
"""

#cars=['nexia','cobalt','jentra','bmw']
#cars.sort()
#for a in cars:
 #   if a=="bmw":
  #      print(a.upper())
   # else:
    #    print(a.title())
#ism=input('Ismingiz nima?\n>>>')
#if ism.lower()!="jamshid":
#    print(f"Uzr, {ism.title()} biz Jamshidni kutyabmiz!")
#else:
 #   print("Salom Jamshid")
#javob=float(input("12*6 nichchaya teng?\n>>>"))
#if javob==72:
 #   print("Javobingiz to'g'ri!")
#else:
 #   print("Javobingiz noto'g'ri")
#yosh=int(input("Yoshingizni kiriting:\n>>>"))
#if yosh>=18:
 #   print("Xush kelibsiz!")
  #  login=input("Yangi login kiriting:\n>>>")
   # if len(login)<=5:
    #    print("Login 5 harfdan uzun bo'lishi shart")
#else:
 #   print("Kirish mumkin emas!!!")
#x=int(input("x="))
#y=int(input("y="))
#print("x>y") if x>y else print("x<y")
cars=['cobalt','bmw','jentra','spark','nexia']
cars.sort()
for a in cars:
    if a=='bmw':
        print(a.upper())
    else:
        print(a.title())
print("!= orqali ishlanishi")
for a in cars:
    if a!='bmw':
        print(a.title())
    else:
        print(a.upper())
a=input("Loginingizni kiriting\n>>>")
if a.lower()=="admin":
    print("Xush kelibsiz, Admin!\nFoydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {a}!")
b=float(input("Birinchi sonni kiriting:"))
c=float(input("Ikkinchi sonni kiriting:"))
if c==b:
    print("Bu sonlar teng ekan.")
else:
    print("Bu sonlar teng emas.")
d=float(input("Son kiriting:"))
if d<0:
    print("Bu son manfiy.")
elif d>0:
    print("Bu son musbat.")
else:
    print("Bu son 0 ga teng.")
print("Ildiz hisoblash dasturi:")
a=float(input("Son kiriting:"))
if a>=0:
    print(f"{a}ning kvadrat ildizi {a**(1/2)}ga teng")
else:
    print("Musbat son kiriting!!!")
    




















      
 
