# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 19:05:45 2023

@author: shoki
"""
class Shaxs:
    def __init__(self,ism,familya,t_yil):
        self.name=ism
        self.surname=familya
        self.t_yil=t_yil
    def get_info(self):
        """Shaxsning malumotlarini chiqaradi"""
        return f"{self.surname} {self.name} {self.t_yil}-yilda tug'ilgan"
    def get_age(self,yil):
        """Hozirgi yilni kiritasiz va bu metod yosh qaytaradi"""
        return yil-self.t_yil
A1=Shaxs("Jamshidbek","Shoirov",2004)
print(A1.get_info())
print(A1.get_age(2023),"\n")
class Talaba(Shaxs):
    def __init__(self,ism,familya,t_yil,pasport,Manzil):
        super().__init__(ism, familya, t_yil)
        self.pasporti=pasport
        self.bosqich=2
        self.Manzili=Manzil
        self.fanlar=[]
    def get_pasport(self):
        return self.pasporti
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        """Talabaningning malumotlarini chiqaradi"""
        return f"{self.surname} {self.name} {self.t_yil}-yilda tug'ilgan. \
Kurs:{self.bosqich}. Pasporti: {self.pasporti}. Manzili:{self.Manzili}"
    def fanga_yozil(self):
        self.fanlar.append()
class get_Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.home=uy
        self.street=kocha
        self.district=tuman
        self.region=viloyat
    def get_manzil(self):
        return f"{self.region} viloyati, {self.district} tumani, {self.street} \
ko'chasi {self.home}-uy"
talaba1_manzil=get_Manzil(8, "Nurjahon", "Yangiariq", "Xorazm")
talaba1=Talaba("Farhod", "Jumayazov", 2004, "AD0417815", talaba1_manzil)
        
    
A2=Talaba("Jamshid","Shoirov",2004,"AD0417816","Toshkent")      
print(A2.get_pasport())
print(A2.get_info(),"\n")   

print(talaba1.get_info())



###########   AMALIYOT  >>>>>>>>>>>>>>>>
class Fan():
    def __init__(self,Nomi):
        self.Nom=Nomi


Fan1=Fan("Matem")



