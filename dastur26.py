# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:22:43 2023

@author: shoki
"""
x=12
print(type(x))
y="dunyo"
print(type(sorted(y)))
print(type(y))

class Talaba:
    def __init__(self,ism, familya, t_yil):
        self.name=ism
        self.surname=familya
        self.year=t_yil
    def names(self):
        return self.name
    def tanishuv(self):
        return (f"Ismim {self.name.title()} {self.surname.title()}, tug'ilgan yilim {self.year}-yil")
            
talaba1=Talaba("Jamshidbek", "Shokirov", 2004)
talaba2=Talaba("Oybek", "Eshonqulov", 2004)
talaba3=Talaba("Jahongir", "rustamov", 2004)
print(talaba1.name)  # BU HAM BO"LADI LEKIN RETURNDAN FOYDALANISH KERAK
print(talaba3.names())
print(talaba2.tanishuv())




########### AMALIYOT>>>>>>>>>>>>
class user:
    def __init__(self, t_ism,foydalanuvchi_ism,email):
        self.fullname=t_ism
        self.users=foydalanuvchi_ism
        self.email=email
    def ismi(self,t_ism):
        
        return t_ism.title()
    def use(self,f):
        return f
    def m(self,e):
        return e
    def get_info(self):
        return (f"Foydalanuvchi: {self.users}; Foydalanuvchi ismi: {self.fullname};\
  Emaili: {self.email}")

x1=input("To'liq ismingizni kiriting:")
x2=input("Foydalanuvchi ismini kiriting:")
x3=input("EMAILingizni kiriting:")
foydalanuvchi1=user(x1,x2,x3)
print(foydalanuvchi1.ismi(x1))
print(foydalanuvchi1.use(x2))
print(foydalanuvchi1.m(x3))
print(foydalanuvchi1.get_info())




