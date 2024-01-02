# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:05:55 2023

@author: shoki
"""
class Talaba:
    def __init__(self,ism, familya, t_yil):
        self.name=ism
        self.surname=familya
        self.year=t_yil
        self.manzil="Xorazm"
    def names(self):
        """Ism qaytaradi"""
        return self.name
    def tanishuv(self):
        """O'zi haqida ma'lumot beradi"""
        return (f"Ismim {self.name.title()} {self.surname.title()}, \
tug'ilgan yilim {self.year}-yil, {self.manzil}da yashayman.")
    def manzili(self):
        """Yashash manzilini qaytaradi"""
        return self.manzil
    def yangi_manzil(self,y_manzil):
        """yangi manzil kiritish imkoniyati"""
        self.manzil=y_manzil
talaba1=Talaba("Jamshidbek","Shokirov",2004)
talaba2=Talaba("Oybek", "Eshonqulov", 2004)
print(talaba1.manzil)
print(talaba1.manzili())
talaba1.manzil="Toshkent"   #  BU USUL TAVSIYA ETILMAYDI!
print(talaba1.manzili())
print(talaba1.tanishuv())

talaba1.yangi_manzil("Yangiariq")
print(talaba1.tanishuv())


class Fan():
    def __init__(self,nomi):
        self.nom=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def add_talaba(self,talaba):
        """Talaba qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
        
    def get_students(self):
        """RO'YXATDAGI HAMMA TALABALARNI ISMINI QAYTARADI"""
        return [x.tanishuv() for x in self.talabalar]
        
        
        
        
matem=Fan("Matematika")
matem.add_talaba(talaba1)
matem.add_talaba(talaba2)

print(matem.talabalar_soni)
print(matem.talabalar[0].name)  # bu usul umuman taqiqlanadi!
print(matem.talabalar[1].tanishuv())

print(matem.get_students())

#########################  AMALIYOT >>>>>>>>>>>>>>>>>>>


class Avto():
    def __init__(self,model,rang,narx,km=0):
        self.modeli=model
        self.rangi=rang
        self.narxi=narx
        self.yili=2021
        self.km=km
        
        
    def get_model(self):
        return self.modeli
    def get_rang(self):
        return self.rangi
    def get_narx(self):
        return self.narxi
    def get_yil(self):
        return self.yili
    def yangi_narx(self,y_narx):
        self.narxi=y_narx
    def get_info(self):
        return f"{self.yili}-yil {self.rangi} {self.modeli}.{self.km}km yurgan. Narxi:{self.narxi}$"
    def updeta_km(self,x):
         self.km=x

car1=Avto("Cobalt","oq",15000)
car2=Avto("Nexia2","oq",5000)
print(car1.get_info())
car1.yangi_narx(16000)
print(car1.get_info())
car2.updeta_km(12000)
print(car2.get_info())



class Avtosalon():
    def __init__(self,nomi,manzili,avtolar):
        self.nom=nomi
        self.manzil=manzili
        self.avto=avtolar
    def name(self):
        return self.nom
    def adress(self):
        return self.manzil
    def cars(self):
        for x in self.avto:
            print(x,end=' ')
        return ''
    def yangi_mashinalar(self,mashina):
        self.avto.append(mashina)
    def malumot(self):
        return f"{self.nom} kompaniyasi {self.manzil}da joylashgan Unda quyidagi mashinalar bor:{self.avto}"
            
M1=Avtosalon("GM", "Uzbekistan",["Cobalt","Jentra","Damas"])
print(M1.name())
M1.yangi_mashinalar("Malibu")
print(M1.cars())     
print(dir(Avto))
print(M1.__dict__)
     
        
        
        
        
        




















